import random

player_score = 0
computadora_score=0
opciones = ("piedra","papel","tijera")

def print_init():
    print("+"*60)
    print("+"*4 + " "*52 + "+"*4)
    print("       Bienvenido al juego de Piedra, Papel o Tijeras")
    print("+"*4 + " "*52 + "+"*4)
    print("+"*60)
    print(" AL GANADOR DE 2 PARTIDAS")
    print(" "*20)

def dibuja_piedra():
    print("     "+"_"*10)
    print("   "+"/"+" "*12 + "\ ")
    print("  "+"/"+" "*14 +   "\ ")
    print("  "+"|"+" "*15 +   "| ")
    print("   "+"\ "+" "*12 + "/ ")
    print("    "+"-"*12)

def dibuja_papel():
    print("    "+"_"*9)
    print("   "+"/"+" "*8 + "/")
    print("  "+"/"+" "*8 +   "/ ")
    print(" "+"/"+" "*8 +   "/ ")
    print(""+"/ "+" "*7 + "/ ")
    print("-"*9)

def dibuja_tijera():
    print("    _    _")
    print("   (_)  (_)")
    print("     \  /")
    print("      \/")
    print("      /\\")
    print("     /  \\")
    print("    /    \\")

def dibuja_vs():
    print("  __        __    _____ ")
    print("  \ \      / /   / ____|")
    print("   \ \    / /   | (___  ")
    print("    \ \  / /     \___ \ ")
    print("     \ \/ /      ____) |")
    print("      \__/      |_____/ ")

def escoja_opcion():
    player_1 = input("Escoja escribiendo su opcion (Piedra, Papel, Tijera): ")
    player_1 = player_1.lower()
    if not player_1 in opciones:
        print("Opcion no disponible, vuelva a intentar")
        player_1=None
        return player_1
    else:
        print("su opcion es: ",player_1)
        return player_1

def computador_opcion():
    computador = random.choice(opciones)
    print("opcion del computador: ",computador)
    return computador

def check_partida(player, computador):
    global player_score
    global computadora_score
    if player == computador:
        print("-- Empate --")
        return None
    if player == "piedra" and computador == "papel":
        computadora_score = computadora_score + 1
        print("Computador gana +1: ",computadora_score)
    if player == "piedra" and computador == "tijera":
        player_score = player_score + 1
        print("Player gana +1: ",player_score)
    if player == "papel" and computador == "piedra":
        player_score = player_score + 1
        print("Player gana +1: ",player_score)
    if player == "papel" and computador == "tijera":
        computadora_score = computadora_score + 1
        print("Computador gana +1: ",computadora_score)
    if player == "tijera" and computador == "papel":
        player_score = player_score + 1
        print("Player gana +1: ",player_score)
    if player == "tijera" and computador == "piedra":
        computadora_score = computadora_score + 1
        print("computador gana +1: ", computadora_score)

def dibuja_opcion(opt):
    if opt == "piedra" :
        dibuja_piedra()
    if opt == "papel" :
        dibuja_papel()
    if opt == "tijera" :
        dibuja_tijera()

def print_score():
    print(f"Puntaje=>  Player: {player_score} / Computador:  {computadora_score}")

def init_Juego():
    print_init()
    print_score()
    round_cont = 1
    while True:
        print(" ")
        print("ROUND ",round_cont)
        print(" ")
        opt_1 = escoja_opcion()
        if opt_1 in opciones:
            dibuja_opcion(opt_1)
            dibuja_vs()
            comp =  computador_opcion()
            dibuja_opcion(comp)
            check_partida(opt_1,comp)
            print_score()
            round_cont +=1
        if player_score >=2 :
            print("*"*80)
            print("GANADOR: PLAYER   SCORE: ",player_score)
            print("*"*80)
            break
        if computadora_score >=2 :
            print("*"*80)
            print("GANADOR: COMPUTADORA   SCORE: ",computadora_score)
            print("*"*80)
            break


init_Juego()



