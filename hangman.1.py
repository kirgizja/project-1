import random
import os
import time

print("Cześć! Zagramy? Trzeba odgadnąć stolicę europejską. \n")
time.sleep(3)
capitals = ["Lizbona", "Madryt", "Vaduz","San Marino","Paryż", "Rzym", "Ateny", "Warszawa",
"Belgrad","Helsinki","Praga", "Oslo", "Kopenhaga", "Berlin","Bratysława", "Wiedeń","Bruksela",
"Zagrzeb","Kijów","Oslo", "Mińsk","Budapeszt", "Sofia", "Andora la Vella","Monaco-Ville", "Ryga",
"Sarajewo", "Tirana", "Podgorica","Tallin", "Amsterdam", "Dublin", "Londyn", "Rejkiawik", "Prisztina",
"Luksemburg", "Wilno", "Skopje", "Valetta", "Moskwa", "Bukareszt", "Lublana", "Watykan"]

word = random.choice(capitals).upper()


correct_letters = "" # poprawne słowa użytkownika
all_letters = ""
lives = 7
still_playing = True


live7 = ''' 
             ! = = = ::
                     ::
                     ::
                     ::
                     ::
            = = = = = =
'''
live6 = ''' 
             ! = = = ::
             O       ::
                     ::
                     ::
                     ::
            = = = = = = 
'''
live5 = ''' 
             ! = = = ::
           _ O       ::
                     ::
                     ::
                     ::
            = = = = = =
'''
live4 = ''' 
             ! = = = ::
           _ O _     ::
                     ::
                     ::
                     ::
            = = = = = = 
'''
live3 = ''' 
             ! = = = ::
           _ O _     ::
             U       ::
                     ::
                     ::
            = = = = = = 
'''
live2 = ''' 
             ! = = = ::
           _ O _     ::
             U       ::
            /        ::
                     ::
            = = = = = =
'''
live1 = ''' 
             ! = = = ::
           _ O _     ::
             U       ::
            / \      ::
                     ::
            = = = = = =
'''
live0 = '''
             ! = = = ::
             O       ::
            /U\      ::
            / \      ::
                     ::
            = = = = = = 
'''         
print()



# def play_hangman(word,lives): - - - - tak ma wyglądać  funkcja
    
while True:

    os.system("cls")
    print(" * * * * * * * * * * * * * ")
    print(" * * * H A N G M A N * * * ")
    print(" * * * * * * * * * * * * * ")

    if lives == 7:
        print(live7)
    elif lives == 6:
        print(live6)
    elif lives == 5:
        print(live5)
    elif lives == 4:
        print(live4)
    elif lives == 3:
        print(live3)
    elif lives == 2:
        print(live2)
    elif lives == 1:
        print(live1)
    elif lives == 0:
        print(live0)
        
    print()

    # trzeba pokazać odgadnięte litery i dać pokreślniki
    # tam, gdzie litery nie zostały odgadnięte

    result = ""

    for letter in word:
        if letter in correct_letters:
            result += letter
        else:
                result += "_ "


    print("           {}".format(result))
    print()
    print()

# trzeba sprawdzić, czy gracz odgadł słowo
  
    if result == word:
        print(" * * * W Y G R Y W A S Z ! * * * ")
        print()
        break

    if lives == 0:
        print("Odgadywane miasto to: ", word)
        print()
        print(" * * * P R Z E G R Y W A S Z  :( * * * ")
        print()
        break
    
 
# pętla, żeby gracz wprowadził literę, która spełni warunek


    while True:
        letter_player_raw = input("Podaj jedną literę: ")
        letter_player = letter_player_raw.upper()
        
        if len(letter_player) < 1 or len(letter_player) > 1:
            print("Podaj jedną literę: ") # powtarzać do znudzenia, żeby gracz wprowadził pojedynczą literę
        elif letter_player in all_letters:
            print("Ta litera już była.")
            print ("Tych liter już nie podawaj: - - - ", all_letters, " - - - ") 
        elif not letter_player.isalpha():
            print("Podaj jedną literę: ") 
        else:
            all_letters += letter_player
            break
        

    # sprawdzić, czy litera odgadnięta przez gracza
    # znajduje się w słowie
    
    if letter_player not in word:
        lives -= 1
    else:
        correct_letters += letter_player


# przerywanie gry na początku? w każdym miejscu? czy po zagraniu 1 raz? a może w kilku miejscach?
# w którym miejsu programu - jeśli na początku to od still_playing = True uzależnić rozpoczęcie
# jeśli w każdym momencie ma być możliwość wyjściae, to w którym miejscu pętli while (mam 2 pętle while)
# i gdzie definiować czy jest True czy 
# jeśli jest break to przerywa i przechodzi do kolejnego fragmentu kodu?

    # still_playing = True
    # #     if input("Jeśli chcesz przerwać napisz 'quit').lower() == "quit":
    #     still_playing = False
    #     break