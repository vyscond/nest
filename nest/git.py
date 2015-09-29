from subprocess import check_output, STDOUT, CalledProcessError


class Repo (object):

    user_name = ['git', 'config', 'user.name']
    user_email = ['git', 'config', 'user.email']
    remote_origin_url = ['git', 'config', 'remote.origin.url']

    def __init__(self, repo):
        self.repo = repo

    def get(self, cmd):
        try:
            return check_output(
                cmd, 
                stderr=STDOUT, 
                timeout=1
            ).decode('utf-8').strip()
        except CalledProcessError:
            return None
