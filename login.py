#dados cadastrados
i = True
senha_cadastrada = 1234
saldo = 10000
numero_usuario = 123
senha_usuario = 1123
nome_usuario = 1
contador_chances = 3
print ("Fundação Bradesco")
print ("Login")
while i:
    numero_do_cartão_c = int(input("insira o numero do cartão: "))
    nome = input("insira seu nome: ")
    senha_cadastrada = int(input("insira sua senha: "))
    if senha_usuario == senha_cadastrada and numero_usuario == numero_do_cartão_c:
        print (f"bem vindo {nome}! saldo atual:R${saldo}")
        saque = float(input("digite o valor que deeja sacar: "))
        while  saldo < saque:
            print (f"saque invalido, saldo atual: R${saldo}")
            saque = float(input("digite um valor valido: "))
        print (f"saque no valor de R${saque} efetuado com sucesso!")
        saldo = saldo - saque
        print (f"saldo atual: R${saldo}")
        i = False
        break
        
    
    contador_chances = contador_chances - 1
    print (f"Erro, tente novamente! Chances restantes {contador_chances} chances")
    if contador_chances == 0:
        print ("Acesso negado! Sua conta foi bloqueada favor consulte a instituição.")
        break   