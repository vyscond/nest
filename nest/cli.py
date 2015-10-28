import argparse


class BaseAction(argparse.Action):

    def __init__(self, **kwargs):
        super(BaseAction, self).__init__(**kwargs)
        self.setup = Setup()

    def __call__(self, parser, namespace, values, option_string=None):
        self.cmd(namespace)
        self.setup.save()

    def cmd(self, namespace):
        raise NotImplementedError(_('.cmd() not defined'))


class GenSetupPy(BaseAction):
    def cmd(self, namespace):
        self.setup.gen()

class Interactive(BaseAction):
    def __init__(self, *args, **kwargs):
        super(Interactive, self).__init__(*args, **kwargs)
        self.NAME = '[nest] project name > '
        self.AUTHOR = '[nest] project author > '
        self.EMAIL = '[nest] author_email > '
        self.VERSION = '[nest] version > '
        self.DESC = '[nest] description > '
        self.LDESC = '[nest] long description (you can pass a path/name of a *.(md|rst)) > '
        self.URL = '[nest] url > '
        self.LICENSE = '[nest] license > '
        self.PKG = '[nest] add packages? (m)anually, (a)uto, (n)ot now > '
        self.PKG_NAME = '[nest] package name (empty to end) > '
        self.PKGS_SELECTION = (
            '{pkgs}\n[nest] enter the indexes you want as' +
            ' requirement separated by space: '
        )
        self.REQ = '[nest] add requiments? (m)anually, (l)ist packages, (n)ot now? '
        self.REQ_NAME = '[nest] requirement name (empty to end) > '
        self.CON_SRPT = '[nest] add now console scripts? (y/n) '

    def cmd(self, namespace):
        # - cli
        self.setup['name'] = input(self.NAME) or BASE_FOLDER
        self.setup['author'] = input(self.AUTHOR) or 'not provided'
        self.setup['author_email'] = input(self.EMAIL) or 'not provided'
        self.setup['version'] = input(self.VERSION) or '0.0.0'
        self.setup['description'] = input(self.DESC) or 'not provided'
        self.setup['long_description'] = input(self.LDESC) or 'not provided'
        self.setup['url'] = input(self.URL) or 'not provided'
        self.setup['license'] = input(self.LICENSE) or 'MIT'
        self.get_packages()
        self.get_requirements()
        self.get_console_scripts()

    def get_packages(self):
        opt = input(self.PKG)
        if opt == 'a' :
            self.setup['packages'] = find_packages(exclude=EXCLUDE_FOLDERS)
        elif opt == 'm':
            while True:
                pkg_name = input(self.PKG_NAME).strip()
                if not pkg_name:
                    break
                self.setup['packages'].append(pkg_name)

    def get_requirements(self):
        # - requirements
        opt = input(self.REQ)
        if opt == 'm' :
            while True :
                requirement = input(self.REQ_NAME)
                if not requirement:
                    break
                self.setup['requirement'] = requirement
        elif opt == 'l' :
            # getting the names of the current packages installed
            pkgs = []
            pkgs_frmt = ''
            for pkg in pip.get_installed_distributions():
                tmp = str(pkg.as_requirement())
                pkgs.append(tmp)
                pkgs_frmt += ''.join('[{idx}] {name}\n'.format(
                        idx=pkgs.index(tmp),
                        name=tmp
                ))
            # preparing to presentation
            indexes = input(self.PKGS_SELECTION.format(pkgs=pkgs_frmt))
            if indexes.isdigit():
                selected_packages = [ int(idx) for idx in indexes.split(' ') ]
                if len(selected_packages) > 0 :
                    self.setup['requiments'] = [ packages[idx] for idx in selected_packages ]

    def get_console_scripts(self):
        # - Console
        if input(self.CON_SRPT) == 'y':
            while True :
                cmd_name = input('[nest] command name > ').strip()
                cmd_mod  = input('[nest] module function > ').strip()
                if cmd_name and cmd_mod :
                    if self.setup.add_console_scripts(cmd_name, cmd_mod) :
                        if input('[nest] another one? (y/n) ') == 'n':
                            break
                    else :
                        if input('you typed it wrong! try again? (y/n) ') == 'n':
                            break

class Extra(BaseAction):

    def cmd(self, namespace):
        pkgs = namespace.packages
        tag = namespace.tag
        try:
            self.setup['extras_require'][tag] += list(
                set(set(pkgs) - self.setup['extras_require'][tag])
            )
        except KeyError as e:
            if e.message == 'extras_require':
                self.setup['extras_require'] = {}
            else:  # tag
                self.setup['extras_require'][tag] = []


class Package(BaseAction):

    def cmd(self, namespace):
        if namespace.action == 'add':
            try:
                self.setup['packages'] += list(
                    set(set(namespace.packages) - self.setup['packages'])
                )
            except Exception:
                self.setup['packages'] = namespace.packages
        elif namespace.action in ['rem', 'del']:
            try:
                for pkg in namespace.packages:
                    self.setup['packages'].remove(pkg)
            except Exception:
                pass


class Version(BaseAction):

    def cmd(self, namespace):
        try:
            old_version = self.setup['version']
        except Exception:
            self.setup['version'] = '0.0.0'
            old_version = self.setup['version']
        version = self.setup['version'].split('.')
        label = { 'major' : 0 , 'minor' : 1 , 'patch' : 2 }[namespace.label]
        if namespace.k < 0 and int(version[label]) < abs(namespace.k) :
            # set directly to zero if the negative K is "bigger" than the current value
            version[label] = '0'
        else :
            version[label] = str(int(version[label])+namespace.k)
        self.setup['version'] = '.'.join(version)
        namespace.k = 'upgrade' if namespace.k else 'downgrade'


def main():

    parser = argparse.ArgumentParser(prog='nest',description='cli to manage setup.py')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser2 = subparsers.add_parser('new', help='%(prog)s will raise a cli to build a new setup.json')
    parser2.add_argument('run', nargs=0, action=Interactive, help=argparse.SUPPRESS)

    parser2 = subparsers.add_parser('gen', help='%(prog)s will raise a cli to build a new setup.json')
    parser2.add_argument('run', nargs=0, action=GenSetupPy, help=argparse.SUPPRESS)

    # parser_gen = subparsers.add_parser('gen', help='%(prog)s will generate a valid setup.py file based on the current setup.json')
    # parser_gen.add_argument('run', nargs=0, action=NestNew, help=argparse.SUPPRESS)

    # - Extras
    parser2 = subparsers.add_parser('extra', help='manage extra requirements for the project')
    parser2.add_argument('action', type=str, help='add or remove')
    parser2.add_argument('tag', type=str, nargs='+', help='extra tag e.g.: "dev", "prod", "tests"... ')
    parser2.add_argument('packages', type=str, nargs='+', help='package(s) name(s)')
    parser2.add_argument('run', nargs=0, action=Extra, help=argparse.SUPPRESS)

    # - Packages
    parser2 = subparsers.add_parser('package', help='manage packages for the project')
    parser2.add_argument('action', type=str, help='add or remove')
    parser2.add_argument('packages', type=str, nargs='+', help='package(s) name(s)')
    parser2.add_argument('run', nargs=0, action=Package, help=argparse.SUPPRESS)

    # - Version
    parser2 = subparsers.add_parser('version', help='manage project version')
    parser2.add_argument('label', type=str, help='major, minor, patch')
    parser2.add_argument('k', type=int, help='amount')
    parser2.add_argument('run', nargs=0, action=Version, help=argparse.SUPPRESS)

    args = parser.parse_args()
