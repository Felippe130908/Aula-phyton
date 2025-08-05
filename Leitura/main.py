def main():
    nome = input ("Digite seu nome: ")
    idade = int ( input ( "Digite sua idade "))
    altura = float (input ("Digite sua altura: "))
    isMasculino = input( "vc é do sexo Masculino? ")

    print("o ", nome, "tem", idade, "anos de idade", altura, "metros de altura")


    if isMasculino == "Sim" or isMasculino == "s":
       print("É Masculino")

    else:
       print("É Feminino")



    return 0
main()

