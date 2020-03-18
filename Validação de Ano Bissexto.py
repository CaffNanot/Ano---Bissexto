#O encontro anual da família Pereira vai acontecer e alguns eventos estão programados:​

#Futebol de Casados x Solteiros da Família*​ 
#Esconde-esconde das crianças​ 
#Almoço​
#Canastra da Família*​
#Cabo de Guerra​
#Bingo dos idosos*​

#Os itens que estão com * são exclusivos da família Pereira.​

print("Bem-vindo(a) ao Encontro Anual da Família Pereira, suas atividades seram determinadas com base nos dados informados abaixo, exceto o almoço que é livre para todos. Bom Evento!")

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
estadoC = input("Digite seu Estado Civil: ")


#if("Pereira" in nome):
    #print("Você é um Pereira")


if(idade <= 10):                                                                                                        #Valida a idade abaixo de 11.
    print("Você participa do Esconde-Esconde das Crianças")
elif(idade >= 11 and idade <=59 and "Pereira" in nome and estadoC == "Solteiro" or estadoC == "Solteira"):              #Valida a idade entre 11 e 59, sendo da Familia e estando solteiro
    print("Você participa da Canastra da Família, do Cabo de Guerra e esta no time dos Solteiros no Futebol")
elif(idade >= 11 and idade <=59 and "Pereira" in nome and estadoC == "Casado" or estadoC == "Casada"):                  #Valida a idade entre 11 e 59, sendo da Familia e estando Casado
    print("Você participa da Canastra da Família, do Cabo de Guerra e esta no time dos Casados no Futebol")
elif(idade >= 11 and idade <=59 and not "Pereira" in nome):                                                             #Valida a idade entre 11 e 59, sem ser da Familia
    print("Você participa do Cabo de Guerra")
elif(idade >=60 and not "Pereira" in nome):                                                                             #Valida a idade acima de 60, sem ser da Familia
    print("Você não participa do Bingo dos Idosos")
elif("Pereira" in nome and idade >=60):                                                                                 #Valida a idade acima de 60, sendo da familia
    print("Você participa do Bingo dos Idosos")





