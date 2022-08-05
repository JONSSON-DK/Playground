import time

from hjælper import draw_board
import random

spots = {1 : "1" , 2 : "2" , 3 : "3" , 4 : "4" , 5 : "5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 : "9"}
numbers = list (range(1,10))

draw_board(spots)

spots = {1 : " " , 2 : " " , 3 : " " , 4 : " " , 5 : " " , 6 : " " , 7 : " " , 8 : " " , 9 : " "}

first = input("Hvor vil du sætte dit X? ")
numbers.remove(int(first))
spots[int(first)] = "X"
draw_board(spots)
print("Så er det min tur")
time.sleep(2)
print("Jeg skal lige tænke lidt over sagerne...")
time.sleep(2)

second = random.choice(numbers)
numbers.remove(int(second))
spots[int(second)] = "O"
draw_board(spots)
print("Så er det din tur")

third = input("Hvor vil du sætte dit X? ")
numbers.remove(int(third))
spots[int(third)] = "X"
draw_board(spots)
print("Så er det min tur")
time.sleep(2)

fourth = random.choice(numbers)
numbers.remove(int(fourth))
spots[int(fourth)] = "O"
draw_board(spots)
print("Så er det din tur")

fifth = input("Hvor vil du sætte dit X? ")
numbers.remove(int(fifth))
spots[int(fifth)] = "X"
draw_board(spots)
print("Uha, du gør det ikke nemt for mig")
time.sleep(2)

sixth = random.choice(numbers)
numbers.remove(int(sixth))
spots[int(sixth)] = "O"
draw_board(spots)
print("Kan du stikke den her!?")

seventh = input("Hvor vil du sætte dit X? ")
numbers.remove(int(seventh))
spots[int(seventh)] = "X"
draw_board(spots)
print("Er du professionel eller hvad!? Jeg er i store problemer...")
time.sleep(2)

eighth = random.choice(numbers)
numbers.remove(int(eighth))
spots[int(eighth)] = "O"
draw_board(spots)
print("Så er det din tur")

ninth = input("Hvor vil du sætte dit X? ")
numbers.remove(int(ninth))
spots[int(ninth)] = "X"
draw_board(spots)
time.sleep(2)
print("Slut prut uafgjort, skal vi prøve igen? :D ")
