import copy

from global_env import DICT_OF_CMDS, DICT_OF_VARS


class Environment:
    # хранит list_of cmd, list_of_var, need_to_exit
    def __init__(self, dict_of_cmds=DICT_OF_CMDS, dict_of_vars=DICT_OF_VARS):
        self._dict_of_cmds = copy.copy(dict_of_cmds)
        self._dict_of_vars = copy.deepcopy(dict_of_vars)

    def get_cmd(self, name):
        if self.cmd_exist(name):
            return self._dict_of_cmds[name]
        else:
            return lambda param, inp, outp, env: self._dict_of_cmds["_external"](name, param, inp, outp, env);

    def get_var(self, name):
        return self._dict_of_vars[name]

    def set_var(self, name, value):
        self._dict_of_vars[name] = value

    def cmd_exist(self, name):
        return name in self._dict_of_cmds
