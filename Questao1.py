#Intervalo 2

N = int(input())

dentro = 0
fora = 0

for i in range(N):
    x = int(input())

    if (x in range(10, 21)):
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')