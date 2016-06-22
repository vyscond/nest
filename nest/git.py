from subprocess import check_output, STDOUT, CalledProcessError
import shlex

class Repo(object):

    user_name = 'git config user.name'
    user_email = 'git config user.email'
    remote_origin_url = 'git config remote.origin.url'

    def __init__(self, repo):
        self.repo = repo

    def get(self, cmd):
        cmd = shlex.split(cmd)
        try:
            ret = check_output(cmd, stderr=STDOUT, timeout=1).decode('utf-8')
            return ret.strip()
        except CalledProcessError:
            return None

    def get_user_name(self):
        return self.get(Repo.user_name)

    def get_user_email(self):
        return self.get(Repo.user_email)

    def get_remote_url(self, label='origin'):
        return self.get('git config remote.{}.url'.format(label))
