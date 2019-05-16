
while (True):
    x = input()

    while(len(x)%2!=0):
        print("even length pls")
        x = input()

    x = x.lower()
    i = 0
    j = len(x)-2
    x = list(x)
    while i < j:
        temp = x[i:i+2]
        x[i] = x[j]
        x[i+1] = x[j+1]

        x[j] = temp[0]
        x[j+1] = temp[1]

        i+=2
        j-=2
    print(''.join(x))
