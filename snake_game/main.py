import pygame as py
import time 
import random

py.init()

# Config e criação da tela
largura = 600
altura = 400
tela = py.display.set_mode((largura, altura))
py.display.set_caption("jogo da Cobrinha")

# Cores do jogo
branco = (255,255,255)
verde = (0,255,0)
preto = (0,0,0)
vermelho = (255,0,0)

# Criação de relogio 
clock = py.time.Clock()
velocidade = 15

# Tamanho do bloco
tamanho_bloco = 20

# Fonte
fonte = py.font.SysFont(None, 35)

# Função de pontuação na tela
def monstrar_pontos(pontos):
    valor = fonte.render("Pontos:", str(pontos), True, preto)
    tela.blit(valor, [10,10])

# Função principal do jogo
def jogo():
    x = largura // 2 
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    # Posição aleatoria da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco)/ 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco)/ 20) * 20

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in py.event.get():
            if evento.type == py.QUIT:
                fim_de_jogo = True
            if evento.type == py.KEYDOWN:
                if evento.key == py.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == py.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == py.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == py.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Atualizar a posicao da cobra
        x += x_mudanca
        y += y_mudanca

        # Verificar se a cobra bateu na borda da tela

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        tela.fill(branco)

        py.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verificar se cobra bateu nela mesma

        for bloco in cobra [:-1]:
            if bloco == cabeca:
                fim_de_jogo = True

        # Desenha todo os blocos 
        for bloco in cobra:
            py.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        # Mostrar a pontuação
        monstrar_pontos(comprimento_cobra - 1)

        py.display.update()

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco)/ 20) * 20
            comida_y = round(random.randrange(0, altura - tamanho_bloco)/ 20) * 20
            comprimento_cobra += 1

        clock.tick(velocidade)

    # Quando o jogo terminar 
    tela.fill(branco)
    mensagem = fonte.render("GAME OVER, PONTUAÇÃO: ", str(comprimento_cobra - 1), True, vermelho)
    tela.blit(mensagem, [largura / 6, altura / 3])
    py.display.update()
    time.sleep(3)
    py.quit()

jogo()