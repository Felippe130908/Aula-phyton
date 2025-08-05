def main():
    idade = int  (input("Digite sua idade: "))
    print("Ele tem", idade, "anos de idade")

    if idade >= 18:
        print("Entrada liberada")

    elif idade >=16:
        acomp = input("você está com algum acompanhate maior de idade? ")
        if acomp == "sim" or acomp == "s": 
            print("Entrada liberada")
         
        else:
            print("Entrada proibida")

    else:
        print("Entrada proibida")
    

    return 0
main()