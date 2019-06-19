from environment import Environment
from parser import *
from settings import SETTINGS


class App:
    '''
        Ответственный за:
        -- запуск приложения
        -- хранении окружения
        -- передачу ответственности по парсигу комманды
        -- передачу ответственности по запуску комманды
    '''

    def __init__(self):
        self.env = Environment()

    def run(self):
        while not self.need_exit():
            try:
                self.before()
                line = input()
                root_cmd = Parser(self.env).run(line)
                root_cmd.run()
            except RuntimeError as e:
                print(e)

    def need_exit(self):
        return self.env.get_var('NEED_EXIT')

    def before(self):
        print(self.env.get_var('print_prefix'), end='')


if __name__ ==  "__main__":
    if SETTINGS['DEBUG']:
        App().run()
    else:
        try:
            App().run()
        except:
            print("Something wrong")
