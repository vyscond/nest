

class Colors :
    WHITE='\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'


def error(msg):
    print('{color}[nest]{end} {msg}'.format(
        color=Colors.RED,end=Colors.END,msg=msg
    ))


def success(msg):
    print('{color}[nest]{end} {msg}'.format(
        color=Colors.GREEN,end=Colors.END,msg=msg
    ))


def debug(msg):
    print('{color}[nest]{end} {msg}'.format(
        color=Colors.WHITE,end=Colors.END,msg=msg
    ))
