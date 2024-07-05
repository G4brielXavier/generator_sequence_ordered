from random import randint
from colorama import Fore, Back

def set_option():
    print()
    print(Fore.WHITE + '//' + Fore.GREEN + 'Help')
    print(Fore.BLUE + 'Range: ' + Fore.WHITE + 'defina até aonde os valores serão gerados.')
    print(Fore.BLUE + 'One-One: ' + Fore.WHITE + 'adicione os valores um por um.')
    print()
    option = input(formatter_input_option('Range', 'One-One')).lower()
    
    if option in ['range', 'one-one']:
        if option == 'range':
            return 'rg'
        else:
            return 'o-o'
        
def formatter_input_option(opt1, opt2):
    return Fore.WHITE + '[ ' + Fore.GREEN + f'{opt1}' + Fore.WHITE + ' | ' + Fore.GREEN + f'{opt2}' + Fore.WHITE + ' ]: '

def set_init():
    init = int(input(Fore.WHITE + ' - Initial: '))
    return init

def set_final(it):
    final = int(input(Fore.WHITE + ' - Final: '))
    if not final == it and final > it:
        return final
    else:
        set_final(it) 
              
def create_seq(opt):
    seq = []
    
    if opt == 'rg':
        initial = set_init()
        final = set_final(initial)
        print('Range of Randomizer ------')
        amg_i = int(input(Fore.GREEN + ' - amg_i: '))
        amg_f = int(input(Fore.GREEN + ' - amg_f: '))

        for i in range(initial, final):
            seq.append(randint(amg_i, amg_f))
        
        print()
        print(Fore.GREEN + 'Generating...')
        print()
        
        for i in seq:
            print(Fore.WHITE + f'{i}', end=' ')
            
    elif opt == 'o-o':
        qty = int(input(Fore.GREEN + ' - Qty: '))
        print()
        for i in range(qty):
            seq.append(int(input(Fore.WHITE + f'Value {i}: ')))
            
        print()
        print(Fore.GREEN + 'Generating...')
        print()
        
        for i in seq:
            print(Fore.WHITE + f'{i}', end=' ')
            
    
    return seq

def des_ordereding(arr):
    last = len(arr)
    
    while last > 0:
        i = 0
        while i < last-1:
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i += 1
        last -= 1
        
    return arr

def ins_ordereding(arr):
    last = len(arr)
    
    while last > 0:
        i = 0
        while i < last-1:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i += 1
        last -= 1
        
    return arr

def des_or_ins(arr):
    print()
    print(Fore.WHITE + '//' + Fore.GREEN + 'Help')
    print(Fore.BLUE + 'Ignore: ' + Fore.WHITE + 'ignora a necessidade de ordenar a sequência.')
    print(Fore.BLUE + 'Do: ' + Fore.WHITE + 'executa a função de ordenação na sequência.')
    print()
    value = input(formatter_input_option('Descending', 'Incresent')).lower()
    if value in ['descending', 'incresent']:
        if value == 'descending':
            new_seq = des_ordereding(arr)
        else:
            new_seq = ins_ordereding(arr)
            
    return new_seq

def do_sort(arr):
    print()
    print(Fore.WHITE + '//' + Fore.GREEN + 'Help')
    print(Fore.BLUE + 'Ignore: ' + Fore.WHITE + 'ignora a necessidade de ordenar a sequência.')
    print(Fore.BLUE + 'Do: ' + Fore.WHITE + 'executa a função de ordenação na sequência.')
    print()
    value = input(formatter_input_option('Ignore', 'Do')).lower()
    if value in ['ignore', 'do']:
        if value == 'ignore':
            print()
            print(Fore.GREEN + 'Ok, Flw')
            return None
        else:
            seq_n = des_or_ins(arr)
            return seq_n
        
def format_dotket():
    print(Back.BLACK + Fore.BLUE + f':] - Dotket ( Gabriel Xavier )')
    print(Back.RESET)