num = int(input('Digite um valor inteiro de 4 digitos para ser criptografado: '))

u = (num //1) % 10
d = (num//10) % 10
c = (num//100) % 10
um = (num//1000) % 10


u = (u+6) % 10
c = (c+6) % 10
d = (d+6) % 10
um = (um+6) % 10

print(f'O número criptografado é: {d}{u}{um}{c}')



def voltar(x):
    if (x % 10) <= 5:
        x += 4
        return x
    else:
        x -= 6
        return x

num2 = int(input('Digite um número de 4 digitos para ser descriptografado: '))

u2 = (num2//1) % 10
d2 = (num2//10) % 10
c2 = (num2//100) % 10
um2 = (num2//1000) % 10

u2 = voltar(u2)
d2 = voltar(d2)
c2 = voltar(c2)
um2 = voltar(um2)

print(f'O número descriptografado é: {d2}{u2}{um2}{c2}')