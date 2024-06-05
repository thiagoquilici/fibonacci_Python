# função fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)
    
try:
    n = int(input('Digite o número que deseja saber sua sequência fibonacci: '))
    if n <= 0:
        print('Por favor, insira um número maior que zero.')
    else:
        print(f'os primeiros {n} da sequência de fibonacci são: ')
        for x in range(n):
            print(f'|{fibonacci(x)}|', end='')
except:
    print('Por favor, insira um número inteiro válido.')
