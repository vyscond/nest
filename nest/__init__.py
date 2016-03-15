import os
import re
import json
import argparse
import pip
import copy
from collections import OrderedDict
from setuptools import find_packages


BASE_FOLDER = os.path.basename(os.path.abspath('.')).replace(' ', '-').lower()
EXCLUDE_FOLDERS = ['contrib','docs','tests*']
TEXT_FILES = '([A-Za-z]+)(\_[A-Za-z]+)*\.(rst|md)$'
SETUPPY = 'from setuptools import setup\nsetup(\n{args}\n)\n'
CONSOLE_SCRIPT = '^([A-Za-z]+)(\_([A-Za-z]+))*\=([A-Za-z]+(\_[A-Za-z]+)*)(\.[A-Za-z]+(\_[A-Za-z]+)*)*\:([A-Za-z]+)(\_([A-Za-z]+))*$'
CLASSIFIERS = ''.join(open('classifiers.txt')).split('\n')


class Setup(OrderedDict):

    def __init__(self):
        self.file = '.setup.json'
        try:
            with open(self.file) as f:
                setup = json.load(f, object_pairs_hook=OrderedDict)
        except IOError:
            setup = OrderedDict()
        super(Setup,self).__init__(setup)

    def __str__(self):  # debug only
        return json.dumps(self, indent=4)

    def save(self):
        with open(self.file, 'w') as f:
            f.write(str(self))

    def add_console_scripts(self, name, module):
        if re.match(CONSOLE_SCRIPT, name+'='+module):
            if 'entry_points' not in self.keys():
                self['entry_points'] = {}
                self['entry_points']['console_scripts'] = {}
            self['entry_points']['console_scripts'][name] = module
        else:
            return 1

    def gen(self):
        '''generates a new setup.py based on your setup.json'''
        setuppy = copy.deepcopy(self)
        # - Adjust console scripts
        setuppy['entry_points']['console_scripts'] = []
        for name, module in self['entry_points']['console_scripts'].items():
            setuppy['entry_points']['console_scripts'].append(
                '{}={}'.format(name, module)
            )
        setuppy = json.dumps(setuppy, indent=4)
        # - Adjust file based entries
        for key in ['long_description']:
            if re.match(TEXT_FILES, self[key]) :
                setuppy=setuppy.replace(
                    '"'+self[key]+'"', '"".join(open("'+self[key]+'"))'
                )
        # - Replacing ":" for "="
        for basekey in self.keys():
            setuppy = setuppy.replace('"'+basekey+'":', basekey+' =')
        setuppy = setuppy[1:-1]
        with open('setup.py', 'w') as f:
            f.write(SETUPPY.format(args=setuppy))



