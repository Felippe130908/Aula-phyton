import random
def main():
    numAle = random.randint(0 , 10)

    num = 11

    i = 0
    while num != numAle:
        num = int( input("Digite um número: "))

        if num < numAle:
            print("o número é maior")
        elif num > numAle:
            print("o número é menor")

            i += 1
            print("\n")

            print("vc acertou! com", i, "tentativas")

    return 0
main()