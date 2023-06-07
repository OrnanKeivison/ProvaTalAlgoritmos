N = int(input())

list = []
tenho = 0

for i in range(N):
    S = input()

    if(S in list):
        tenho += 1
    else:
        list.append(S)


    print(list)

print(f'Falta(m) {151-len(list)} pomekon(s).')
