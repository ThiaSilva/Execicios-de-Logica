nome = input("Qual o nome do Heroi: ")
nivel = ["Ferro","Bronze","Prata","Ouro","Platina","Ascendente","Imortal","Radiante"]

def nivelHeroi():
  qtdXP = int(input("Qual a quantidade de XP: "))
    
  if(qtdXP < 1000):
    print(f"O Herói de nome {nome} está no nível de {nivel[0]}")
  elif (qtdXP >= 1001 and qtdXP <= 2000):
    print(f"O Herói de nome {nome} está no nível de {nivel[1]}")
  elif (qtdXP >= 2001 and qtdXP <= 5000):
    print(f"O Herói de nome {nome} está no nível de {nivel[2]}")
  elif (qtdXP >= 5001 and qtdXP <= 7000):
    print(f"O Herói de nome {nome} está no nível de {nivel[3]}")
  elif (qtdXP >= 7001 and qtdXP <= 8000):
    print(f"O Herói de nome {nome} está no nível de {nivel[4]}")
  elif (qtdXP >= 8001 and qtdXP <= 9000):
    print(f"O Herói de nome {nome} está no nível de {nivel[5]}")
  elif (qtdXP >= 9001 and qtdXP <= 10000):
    print(f"O Herói de nome {nome} está no nível de {nivel[6]}")
  elif (qtdXP >= 10001):
    print(f"O Herói de nome {nome} está no nível de {nivel[7]}")

nivelHeroi()