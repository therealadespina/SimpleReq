alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
base = len(alphabet)

length = 0
counter = 0

#counter -> number16

while counter < 3866000:

    #counter -> number16 = password
    #1000 -> [3, 14, 8] -> 3e8

    password = ""
    c = counter
    while c > 0:
        rest = c % base
        c = c // base
        password = alphabet[rest] + password

    while len(password) < length:
        password = "0" + password

    print (counter, password)

    if password == "z" * length:
        length += 1
        counter = 0
    else:
        counter += 1
