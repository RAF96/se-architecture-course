from cmds.grep import Grep
from cmds.implementation_cmd import *
from cmds.implementation_internal_cmd import _nothing, _assignment_operator, _external

DICT_OF_CMDS = {
    'cat': cat,
    'exit': exit,
    'echo': echo,
    'wc': wc,
    'pwd': pwd,
    'grep': Grep(),
    '_assignment_operator': _assignment_operator,
    '_nothing': _nothing,
    '_external': _external
}

DICT_OF_VARS = {
    'NEED_EXIT': False,
    'print_prefix': ">> "
    #'test_file': "/home/raf/tmp/code.hs" # need for debug. delete in release
}

