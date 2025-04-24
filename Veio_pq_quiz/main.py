
# Começo do quiz
print("Bem-vindo ao Veio pq Quiz!")

# Perguntar para o Usuario se ele quer jogar
answer_user = input("Você esta pronto para o quiz? (S/N) ")

# Verificação caso o usuario nao queria jogar
if answer_user != "S":
    quit()

score = 0

# Estrutura do quiz
print("Começando...")
print("Quem é foi o campeão brasileiro em 2017? \n (A) Flamengo \n (B) Bahia \n (C) Corinthians \n (D) Internacional \n")            
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposata Incorreta!")

print("Em que ano a seleção brasileira ganhou sua ultima copa do mundo? \n (A) 2018 \n (B) 1962 \n (C) 1998 \n (D) 2002 \n")            
answer_2 = input("Resposta: ")

if answer_2 == "D":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposata Incorreta!")

print("Quem é o maior campeao da Champios League? \n (A) Real Madird \n (B) Milan \n (C) Ajax \n (D) Estrela Vermelha \n")            
answer_3 = input("Resposta: ")

if answer_3 == "A":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposata Incorreta!")

print("Quem foi o artilehiro da Champions league em 2023/2024? \n (A) Mbappe \n (B) Messi \n (C) Raphinha \n (D) Vinicius Junior \n")            
answer_4 = input("Resposta: ")

if answer_4 == "A":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposata Incorreta!")

print("Qual o clube com mais titulos da copa do brasil? \n (A) Gremio \n (B) Palmeiras \n (C) Flamengo \n (D) Cruzeiro \n")            
answer_5 = input("Resposta: ")

if answer_5 == "D":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposata Incorreta!")


# Mostrar pontuação
print(f"O Quiz acabou Pontuação: {score}/5")

