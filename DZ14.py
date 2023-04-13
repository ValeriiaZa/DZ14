number = int(input('Type any digit:'))
x = 1
i = 1
if number >= 0:
    while number > 9:
        cnt = len(str(number))
        x = number // 10 ** (cnt - i)
        while True:
            i += 1
            x *= (number // 10 ** (cnt - i) % 10)
            if cnt == i:
                break
            else:
                continue
        number = x
        i = 1
    else:
        print(number)
else:
    print('Error')

