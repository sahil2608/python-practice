# Prime number between ny 2 range

low = int(input("Enter lower range"))
high = int(input("Enter upper range"))

for i in range(low, high):
    for j in range(2, int(i/2)):
        if i%j == 0:
            break
    else:
        print(i)

