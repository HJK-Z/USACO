def basechange(num, base):
    numstr = str(num)
    total = 0

    for i in range(len(numstr)):
        a = int(numstr[len(numstr)-1-i])
        total += a * base**i

    return total

def sol():
    for i in range(len(b2istr)):
        a = int(b2istr[i])
        flip = int((a + 1) % 2)
        nb2 = b2istr[0:i] + str(flip) + b2istr[i + 1:]

        b2b10 = basechange(nb2, 2)

        for j in range(len(b3istr)):
            b = int(b3istr[j])
            flip1 = int((b + 1) % 3)
            flip2 = int((b + 2) % 3)
            nb31 = int(b3istr[0:j] + str(flip1) + b3istr[j + 1:])
            nb32 = int(b3istr[0:j] + str(flip2) + b3istr[j + 1:])

            b3b101 = basechange(nb31, 3)
            b3b102 = basechange(nb32, 3)

            if b2b10 == b3b101:
                print(b2b10)
                return

            if b2b10 == b3b102:
                print(b2b10)
                return


b2istr = input()
b3istr = input()

sol()



