

def _assignment_operator(parameters, input_stream, output_stream, env):
    '''
        Название для оператора присваевания =.
    '''
    env.set_var(parameters[0].text, parameters[1].text)


def _nothing(parameters, input_stream, output_stream, env):
    '''
        Команда, которая ничего не делает
    '''
    return


def _external(name, parameters, input_stream, output_stream, env):
    '''
        внешняя команда. Используется, когда другой комманды не нашлось
    '''
    import subprocess
    subprocess.call(name, stdout=output_stream)
