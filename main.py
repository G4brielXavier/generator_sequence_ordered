from func.gets import *

format_dotket()
opt_init = set_option()

print()
seq_generated = create_seq(opt_init)

print()

n_seq = do_sort(seq_generated)
print()

if n_seq is not None:
    for i in n_seq:
        print(Fore.WHITE + f'{i}', end=' ')