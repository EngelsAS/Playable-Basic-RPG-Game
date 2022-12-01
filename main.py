import random

print("|Você foi enviado em uma jornada para entregar uma carta importante para um rei em seu palacio. \n|Os reinos estão em guerra, essa carta carrega uma proposta de paz para que o rei em questão não inicie um ataque contra o reino onde você vive")
print("|Devido a situação de guerra que os reinos se encontram, a entrada principal e os muros do castelo\n|Estão sendo protegidos por criaturas sobrenaturais a mandado do rei")
print("|É impossivel entrar no castelo de maneira convencional, o rei nao abrira as portas para um mensageiro do reino inimigo a nenhum custo\n|É preciso invadir")
print("|Você foi informado antes de sair em sua jornada que existe um casebre a 1 quilometro do castelo, lá se encontra um alçapão que da acesso ao castelo")
print("|Esse alçapão serve como saída de emergencia para os residentes do palacio\n|Porém nao será tão facil, dizem que no meio dessa passagem subterranea existe uma fera milenar\n|que tem a unica tarefa de impedir qualquer pessoa de outro reino de entrar por aquela passagem")
print("|Você está equipado com uma armadura da infantaria, uma espada de prata derivada de um ritual sagrado para dar poderes misticos a armas\n|(Porém você desconhece a eficacia de tal ritual...)")
print("|Você tambem leva consigo um escudo, uma mochila com poções de cura e um livro de feitiços te dado de ultima hora por um mago do seu reino\n|(Porém você só aprendeu a conjurar apenas um feitiço de fogo então não sei se será tão util assim")
print("|É hora de decidir, vc irá ate a casa e entrará pelo alçapão ou ira desistir de sua missão?\n|(ir/desistir)")
decisao = input()
print("")
if(decisao == "ir"):
    print("|Você decide enfrentar a sua missão e caminha ate o casebre que você vê ao longe\n|A casa está vazia...você procura e finalmente acha o alçapão que lhe dará acesso ao palacio, deseja entrar?\n|(sim/não)")
    decisao = input()
    print("\n")

    if(decisao == "sim"):
        print("|Muito bem, a escolha é sua...")

    else:
        print("|Você ja andou até aqui e eu tô sem tempo pra narrar uma historia diferente se você for por outro caminho...vamos lá")

    print("|Você adentra no alçapão e se vê em um corredor subterrâaneo escuro\n|Você tira uma tocha da sua mochila e a acende pra iluminar o caminho tortuoso pelo qual irá passar agora")
    print("|Muito bem, aqui a sua verdadeira jornada começa\n|Eu gostaria de saber seu nome pra que eu possa saber exatamente quem é o grande herói dessa jornada")
    nickname = input("|Escreva seu nome: ")
    print("\n")
    print("|Muito bem "+nickname+" vamos seguir em frente nesse corredor tortuoso, você não tem muita escolha mesmo...")
    print("|Você avança com calma pois sabe que existe uma fera milenar, monstruosa, sanguinaria\n|Te esperando em algum lugar (bem pelo menos é oq as lendas dizem)")
    print("|Na medida que você avança, você começa escutar algo que aparenta ser um miado de um gato\n|Quer avançar mais pra descobrir de onde vem o barulho?\n|(sim/não)")
    decisao = input()
    print("")

    if(decisao == "sim"):
        print("|Você avança e se aproxima do barulho, pra sua surpresa era realmente um gato, um gatinho preto")

    else:
        print("|Você está com medo, decide não avançar, porém, o barulho avança lentamente até você...\n|Pra sua surpresa era realmente um gato, um gatinho preto")
        
    print("|Que estranho um gato nesse local, mas tudo bem. Você se inclina pra fazer carinho no gato...\n|O gato parece se sentir incomodado e te ataca! Mas que estranho, o ataque desse gatinho te machucou mais do que o normal")
    print("|Você se afasta levemente do gato e o observa se preparando pra te atacar novamente\n|O gato novamente te ataca e desse vez te machuca ainda mais. Você observa uma movimentação estranha no corpo do gato...")
    print("|Os olhos do gato parecem estar mudando de formato e o seu corpo parece estar aumentando levemente de tamanho\n|Ele parece mais imponente e se prepara pra atacar novamente...\n|Ele pula violentamente pra te atacar, mas você empunha seu escudo e se defende\n|A batalha se inicia...")
    print("\n")
    print("|-----------------------------|\n|Tutorial de batalha          |\n|-----------------------------|\n|Você tem 4 opções:           |\n|1-Atacar                     |\n|2-Defender                   |\n|3-Magia(Fogo)                |\n|4-Mochila(Uso de Poções)     |\n|-----------------------------|")
    print("|Cada número equivale a sua   |\n|Respectiva ação              |\n|Por exemplo: 1 = atacar      |\n|Ao fazer ações de combate    |\n|Um dado de 6 lados será      |\n|Lançado definindo sua sorte  |\n|Para realizar a ação         |\n|-----------------------------|")
    suavida = 100
    vidainimigo = 100
    dano = 50
    cura = 5
    print("")

    while(suavida > 0 and vidainimigo > 0):
        print("|------"+nickname+"------|           |------Gato------|\n|        "+str(suavida)+"       |           |       "+str(vidainimigo)+"      |")
        print("|-----------------------------|\n|1-Atacar                     |\n|2-Defender                   |\n|3-Magia(Fogo)                |\n|4-Mochila(Uso de Poções)     |\n|-----------------------------|")
        print("")
        decisao = int(input("Escolha o número equivalente a ação que deseja realizar: "))
        print("")
        dado = random.randint(1,7)
        if(decisao == 1):
            print("|Decidiu atacar")
            if(dado == 1):
                print("|"+nickname+"...sinto lhe dizer, mas, você ta sem sorte\n|O resultado da rolagem de dados foi "+str(dado))
                print("|Você tenta acertar o inimigo, mas falha miseravelmente, se atrapalha ao empunhar sua espada e acaba se arranhando com a propria...\n|Recebeu "+str(dano - 48)+" de dano")
                suavida = suavida - (dano - 48)
            elif(dado == 2 or dado == 3):
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe fraco no inimigo e da "+str(dano - 38)+" de dano")
                vidainimigo = vidainimigo - (dano - 38)
            elif(dado == 4 or dado == 5):
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe forte no inimigo e da "+str(dano - 26)+" de dano")
                vidainimigo = vidainimigo - (dano - 26)
            else:
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe DEVASTADOR no inimigo e da "+str(dano - 18)+" de dano")
                vidainimigo = vidainimigo - (dano - 18)
        elif(decisao == 2):
            if(dado == 1):
                print("Tirou "+str(dado)+" sinto lhe informar mas o inimigo ira te acertar em cheio\n|Reze pra que a rolagem de dados dele seja tão ruim quanto a sua..." )
                dado = random.randint(1,7)
                if(dado == 1 and vidainimigo > 0):
                    print("|Seu inimigo ta com azar...a rolagem de dado deu "+str(dado)+" ele errou o ataque")
                elif(dado == 2 or dado == 3 and vidainimigo > 0):
                    print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque fraco e te causou "+str(dano - 48)+" de dano")
                    suavida = suavida - (dano - 48)
                elif(dado == 4 or dado == 5 and vidainimigo > 0):
                    print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque forte e te causou "+str(dano - 46)+" de dano")
                    suavida = suavida - (dano - 46)
                else:
                    if(vidainimigo > 0):
                        print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque DEVASTADOR e te causou "+str(dano - 43)+" de dano")
                        suavida = suavida - (dano - 43)
            else:
                print("Você conseguiu se defender perfeitamente do ataque inimigo")
        elif(decisao == 3):
            if(dado == 1):
                print("|É "+nickname+", você ta sem sorte. A rolagem de dado deu "+str(dado)+"\n|Você ate consegue soltar a magia, mas se atrapalha tanto a conjurando que acaba queimando a ponta do proprio dedo...\n|Você recebeu "+str(dano - 45)+" de dano")
                suavida = suavida - (dano - 45)
            elif(dado == 2 or dado == 3):
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama fraca no inimigo e da "+str(dano - 35)+" de dano")
                vidainimigo = vidainimigo - (dano - 35)
            elif(dado == 4 or dado == 5 ):
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama forte no inimigo e da "+str(dano - 20)+" de dano")
                vidainimigo = vidainimigo - (dano - 20)
            else:
                print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama DEVASTADORA no inimigo e da "+str(dano - 10)+" de dano")
                vidainimigo = vidainimigo - (dano - 10)
        else:
            if(cura > 0):
                print("|Você usou uma poção e se curou em 30 pontos de vida")
                cura -= 1
                suavida = suavida + 15
            else:
                print("|Você não tem poções na mochila")

        if(vidainimigo > 0):
            print("|Agora é o turno do inimigo")
        dado = random.randint(1,7)

        if(dado == 1 and vidainimigo > 0):
            print("|Seu inimigo ta com azar...a rolagem de dado deu "+str(dado)+" ele errou o ataque")
        elif(dado == 2 or dado == 3 and vidainimigo > 0):
            print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque fraco e te causou "+str(dano - 48)+" de dano")
            suavida = suavida - (dano - 48)
        elif(dado == 4 or dado == 5 and vidainimigo > 0):
            print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque forte e te causou "+str(dano - 46)+" de dano")
            suavida = suavida - (dano - 46)
        else:
            if(vidainimigo > 0):
                print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque DEVASTADOR e te causou "+str(dano - 43)+" de dano")
                suavida = suavida - (dano - 43)

        if(vidainimigo <= 50):
            print("|Alguma coisa está acontecendo com o gato...ele está crescendo mais e mais\n|Está claramente mudando sua forma. Penas começam a surgir em seu pescoço\n|O focinho está se tornando um bico de aguia, asas de ave saem das costas da criatura\n|Mas o torso da criatura ainda é de um felino, porem...não mais de um gato...a criatura tem o torso de um leão!\n|Não restam duvidas, aquele pequeno gato tinha agora se tornado um enorme GRIFO!")
            print("|A batalha tomou um novo nivel de dificuldade...LUTE "+nickname+", VENÇA ESSA CRIATURA")
            vidainimigo = 200
            while(suavida > 0 and vidainimigo > 0):
                print("|------Engels------|           |------Gato------|\n|        "+str(suavida)+"       |           |       "+str(vidainimigo)+"      |")
                print("|-----------------------------|\n|1-Atacar                     |\n|2-Defender                   |\n|3-Magia(Fogo)                |\n|4-Mochila(Uso de Poções)     |\n|-----------------------------|")
                print("")
                decisao = int(input("Escolha o número equivalente a ação que deseja realizar: "))
                print("")
                dado = random.randint(1,7)
                if(decisao == 1):
                    print("|Decidiu atacar")
                    if(dado == 1):
                        print("|"+nickname+"...sinto lhe dizer, mas, você ta sem sorte\n|O resultado da rolagem de dados foi "+str(dado))
                        print("|Você tenta acertar o inimigo, mas falha miseravelmente, se atrapalha ao empunhar sua espada e acaba se arranhando com a propria...\n|Recebeu "+str(dano - 48)+" de dano")
                        suavida = suavida - (dano - 48)
                    elif(dado == 2 or dado == 3):
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe fraco no inimigo e da "+str(dano - 38)+" de dano")
                        vidainimigo = vidainimigo - (dano - 38)
                    elif(dado == 4 or dado == 5):
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe forte no inimigo e da "+str(dano - 26)+" de dano")
                        vidainimigo = vidainimigo - (dano - 26)
                    else:
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta um golpe DEVASTADOR no inimigo e da "+str(dano - 18)+" de dano")
                        vidainimigo = vidainimigo - (dano - 18)
                elif(decisao == 2):
                    if(dado == 1):
                        print("Tirou "+str(dado)+" sinto lhe informar mas o inimigo ira te acertar em cheio\n|Reze pra que a rolagem de dados dele seja tão ruim quanto a sua..." )
                        dado = random.randint(1,7)
                        if(dado == 1 and vidainimigo > 0):
                            print("|Seu inimigo ta com azar...a rolagem de dado deu "+str(dado)+" ele errou o ataque")
                        elif(dado == 2 or dado == 3 and vidainimigo > 0):
                            print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque fraco e te causou "+str(dano - 40)+" de dano")
                            suavida = suavida - (dano - 48)
                        elif(dado == 4 or dado == 5 and vidainimigo > 0):
                            print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque forte e te causou "+str(dano - 30)+" de dano")
                            suavida = suavida - (dano - 46)
                        else:
                            if(vidainimigo > 0):
                                print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque DEVASTADOR e te causou "+str(dano - 21)+" de dano")
                                suavida = suavida - (dano - 43)
                    else:
                        print("Você conseguiu se defender perfeitamente do ataque inimigo")
                elif(decisao == 3):
                    if(dado == 1):
                        print("|É "+nickname+", você ta sem sorte. A rolagem de dado deu "+str(dado)+"\n|Você ate consegue soltar a magia, mas se atrapalha tanto a conjurando que acaba queimando a ponta do proprio dedo...\n|Você recebeu "+str(dano - 45)+" de dano")
                        suavida = suavida - (dano - 45)
                    elif(dado == 2 or dado == 3):
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama fraca no inimigo e da "+str(dano - 35)+" de dano")
                        vidainimigo = vidainimigo - (dano - 35)
                    elif(dado == 4 or dado == 5 ):
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama forte no inimigo e da "+str(dano - 20)+" de dano")
                        vidainimigo = vidainimigo - (dano - 20)
                    else:
                        print("|O resultado do dado foi "+str(dado)+"\n|Você acerta uma chama DEVASTADORA no inimigo e da "+str(dano - 10)+" de dano")
                        vidainimigo = vidainimigo - (dano - 10)
                else:
                    if(cura > 0):
                        print("|Você usou uma poção e se curou em 30 pontos de vida")
                        suavida = suavida + 30
                    else:
                        print("|Você não tem poções na mochila")

                if(vidainimigo > 0):
                    print("|Agora é o turno do inimigo")
                    
                    dado = random.randint(1,7)

                    if(dado == 1 and vidainimigo > 0):
                        print("|Seu inimigo ta com azar...a rolagem de dado deu "+str(dado)+" ele errou o ataque")
                    elif(dado == 2 or dado == 3 and vidainimigo > 0):
                        print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque fraco e te causou "+str(dano - 40)+" de dano")
                        suavida = suavida - (dano - 40)
                    elif(dado == 4 or dado == 5 and vidainimigo > 0):
                        print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque forte e te causou "+str(dano - 30)+" de dano")
                        suavida = suavida - (dano - 30)
                    else:
                        if(vidainimigo > 0):
                            print("|A rolagem de dado do inimigo deu "+str(dado)+" Seu inimigo te acertou com um ataque DEVASTADOR e te causou "+str(dano - 21)+" de dano")
                            suavida = suavida - (dano - 43)
    print("")
    if(suavida > 0):
        print("|Depois de uma ardua batalha, você derrotou a fera! Parabens! "+nickname+"!")
        print("|Antes que a adrenalina baixasse, você começa a escutar tropas marchando para se reunir em frente ao palacio\n|Você precisa ser rapido, o ataque ao seu reino ja está sendo preparado...\n|Sem tempo pra recuperar o folego, você corre ofegante ate o fim do corredor e encontra uma escada que te levará ate o palacio")
        print("|Você sobe pela escada e entra no palacio, porem, não sera um caminho facil, é possivel ver guardas rondando o caminho que te levará até o rei...\n|Porém, você não tem mais tempo para pensar em uma estrategia para passar despercebido, afinal, você ainda é visto como um intruso de outro reino\n|Com as tropas do rei se organizando pra atacar e sem tempo para pensar, você corre incessantemente em direção as escadas que levam ao trono...\n|Você é visto pelos guardas, porem continua a correr e subir as escadas...você não ira desistir\n|Em uma tentativa desesperada, você puxa a carta do bolso e a ergue enquanto corre...você chega ao grande tapete vermelho que te levará ao rei\n|Vendo o rei ao longe, você fica esperançoso e corre desesperadamente, porem, os guardas desse andar tambem percebem sua presença e correm ate você\n|O rei, ao longe, ao perceber aquele alarde, tem a atenção roubada pela sua correria para encontra-lo e percebe que você leva uma carta em uma das mãos\n|Porem, antes de dar qualquer ordem para acalmar os guardas...um deles consegue te alcançar e você é atingido no abdomem por uma espada\n|Em sequencia, todos os outros guardas fincam a espada em seu torso, dando um fim a sua vida...\n|O rei ainda confuso com a cena e tendo ideia de que você trazia uma carta em mãos, se levanta, vai até o seu cadaver e toma a carta de seu corpo...\n")
        print("|Ao ler a carta ensanguentada, o rei imediatamente corre para descer as escadas e ir até o portão do palacio onde as tropas se encontram\n|E erguendo a carta para cima, anuncia que não haverá mais guerra entre os reinos, estamos em paz novamente...")
        print("|Semanas após esse acontecimento começaram a erguer uma estatua em sua homenagem no reino onde você residia\n|Você morreu em sua missão, porem, nunca morrerá na mente do seu povo e na historia do seu reino...\n|Você concluiu sua missão, salvou seu reino e se eternizou como "+nickname+", O Herói da nação")
        print("---------------------------------------------------------------------------FIM---------------------------------------------------------------------------")
        input()


    else:
        print("|Você lutou bravamente, mas não conseguiu ser pareo para a força da criatura...infelizmente, sua jornada acaba aqui\n|Você não conseguiu completar sua missão e seu reino foi devastado pelas forças inimigas...")
        print("---------------------------------------------------------------------------FIM---------------------------------------------------------------------------")
        input()

else:
    print("|Você desiste da sua missão e volta cabisbaixo para o seu reino\n|Ao se dirigir ao seu rei para contar de seu fracasso, você é acusado de desertar de sua missão e trair seu reino\n|Você é condenado a prisão no calabouço...")
    print("|No dia seguinte os guardas vão até a sua cela para te avisar que sua sentença mudou, você não ficara mais preso no calabouço\n|O rei decidiu te sentenciar com a morte em local publico para que você sirva de exemplo para os outros que pensem em desistir")
    print("|O seu rei infelizmente não é dos mais piedosos...\n|Sua jornada acaba aqui de forma tragica e vergonhosa...")
    print("---------------------------------------------------------------------------FIM---------------------------------------------------------------------------")              
    input()