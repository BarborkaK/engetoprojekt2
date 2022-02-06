import random


def pozdrav():
    text_pozdrav = """
    Hi there!
  -----------------------------------------------
  I've generated a random 4 digit number for you.
  Let's play a bulls and cows game.
  -----------------------------------------------
  Enter a number:
  -----------------------------------------------
  """
    print(text_pozdrav)


def tajne_cislo():
    for i in range(4):
        x = random.randint(0, 9)
        cislo.append(x)
    if len(cislo) > len(set(cislo)):
        cislo.clear()
        tajne_cislo()


def hra():
    global pokusy
    pokusy += 1
    cows = 0
    bulls = 0
    # print(cislo)

    while True:
        volba_cisla = input("Zvol si 4místné a neopakuj cisla")
        if len(volba_cisla) != 4:
            continue

        if len(list(set(volba_cisla))) != 4:
            continue

        break

    hrac = []

    for i in range(4):
        hrac.append(int(volba_cisla[i]))

    bulls_list = []
    for x in range(4):
        if hrac[x] == cislo[x]:
            bulls += 1
            bulls_list.append(hrac[x])

    for c in hrac:
        if c in cislo and c not in bulls_list:
            cows += 1

    print("Bulls:", bulls)
    print("Cows:", cows)
    if bulls == 4:
        print(f"Vyhrál si po {pokusy} pokusech")
    else:
        hra()


pozdrav()
while True:
    cislo = []
    pokusy = 0

    tajne_cislo()
    hra()

    i = input('Chces hrat znovu ?')

    if i != 'y':
        break