def UnpackIntoList(argsTuple: tuple) -> list:
    """
    Utility function, takes all arguements given into a tuple and converts them into a list.

    Inputs:
        args_tuple (tuple) the parsed "*args" .
    Outputs:
        args_list (list) the resulting list.
    """
    args_list = []

    for index, value in enumerate(argsTuple):
        if index != 0:
            args_list.append(value)
    
    return args_list

def command(command_func):
    def wrapper(*args):

        args_list = UnpackIntoList(args)

        command_func(args)
       
    return wrapper


@command
def Say(mensagem):
    print(mensagem + " linha 9")

@command
def Sum(numeros):

    total = 0

    for numero in numeros:
        total += int(numero)
    
    print(total)

while True:
    comando = input("$ ")

    if comando.lower() == "brk":
        break
    if comando.lower().split()[0] == "say":
        Say(comando)
    if comando.lower().split()[0] == "sum":
        Sum(comando)
        