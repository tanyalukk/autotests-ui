result = 0

while True:
    text = input()
    result += 1
    if text == 'стоп' or text == 'хватит' or text == 'достаточно' :
        break


print(result)


email = input()

while not ('_' in email):
    email = input()
    if '_' in email:
        print(email)

while True:
    nickname = input()
    if '_' not in nickname:
        print(nickname)
        break