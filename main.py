#tst push
#test pull
import time, random, os,  sys
from dialoge_notes import death_wish

#colours 
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
RESET = "\033[0m"
#when player dies
def die(mesg):
    print(f"\n{R} -YOU DIED- {RESET}")
    print(mesg)
    print(death_wish)
    sys.exit()


def winmesg(m):
    print(f"\n{G}-YOU SURVIVED-{RESET}\n{m}")


def clear():
    
    os.system('clear')

#game starts here, intro
clear()
print(f"{R}VEXING VOLCANO v1 \U0001F30B {RESET}")
u = input("Name? ").strip() or "skipper"
#intro 'cutscene'
print(f"\nhey {u}. you fell out of a helicopter into Vexing volcano.")
if input("Read the scibblings on wall? enter to skip (y/n) ").lower() == 'y':
    print("\nit insults your intelligence for falling into the volcano")
    input(G + "press enter to start game" + RESET)
#real game start
clear()
print("You're on a ledge. It's hot. \n1) Climb\n2) Eat mushrooms you found growing on wall\n3) Scream for help")
choice = input("- ")

if choice == "1":
    sub = "" 
    playerh = 42
    golemhealth = 32
    print("Climbing")
    time.sleep(2)
    print("Found a ledge")
    sub = input("1. Run  2. Treasure 3. Slide: ")
    if sub == "1":
            winmesg("You made it out and finally feel fresh air")
    elif sub == "2":
         chest = input("You found a shiny golden chest. Open it? (Y/N)-- ").lower()
         if chest == "y":
            clear()
            print("You found a wooden spear.")
            Inventory.append("wooden spear")
            print("Spear added to bag...")
            time.sleep(2)
            print("as you open the chest a golem sneaks up on you...")
            time.sleep(2)
            print(f"\n{R} ITS GONNA ATTACK YOU {RESET}")
    else:
        die("The chest explodes as you walk away.")
        clear()
    def big_fight():
   
     playerh = 42
     golemhealth = 32

    while playerh > 0 and golemhealth > 0:

        print("\nYour Health:", playerh)
        print("Golems health:", golemhealth)
        print("1 attack \U00002694")
        print("2 heal \U0001F9E1")

        move = input("- ")

        if move == "1":
            atkdmg = random.randint(3, 7)
            golemhealth = golemhealth - atkdmg
            print("You hit the golem for", atkdmg)

        elif move == "2":
            heal = random.randint(4, 10)
            playerh = playerh + heal
            print("You healed for", heal)

        else:
            print("You did nothing")

        if golemhealth > 0:
            goldmg = random.randint(4, 9)
            playerh = playerh - goldmg
            print("The golem smacks you for", goldmg)

        time.sleep(2)

    if playerh > 0:
        print("You somehow managed to beat the golem")
        winmesg("You make it out of the volcano covered in rock bits.")
        fighting = False
    elif "wooden spear in inventory":
            print ("the golem attempted to kill you, you pulled your spear out to keep the fight going")
    else:
        die("The golem crushes you")
elif choice == "2":
    clear()
    print("Glowing mushrooms looks tasty")
    mush = input("Red or Blue? ").lower()
    if "red" in mush:
        if random.choice([True, False]):
            winmesg("You grew wings and flew out of the volcano")
        else:
            die("You turned into a rock. Someone's gonna skip you later.")
    else:
        die("You're a museum exhibit now. Don't move.")

        if sub.lower() == "n":
            die("the chest exploded as you turned to walk away from it")
            
        else:
            die("you went down a slide you found right into lava")
       
        
        
        #first minigame path
        
elif choice == "3":
    clear()
    print("You scream for help")
    time_time = 2
    print("A huge golem jumps out of the lava \U0001F608")
    print(f"{R}it looks like its gonna attack you {RESET}")
    
    playerh = 42
    golemhealth = 32

    while playerh > 0 and golemhealth > 0:

        print("\nYour Health:", playerh)
        print("Golems health:", golemhealth)
        print("1 attack \U0001F9E1")
        print("2 heal \U00002694")

        move = input("- ")

        if move == "1":
            atkdmg = random.randint(2, 6)
            golemhealth = golemhealth - atkdmg
            print("You hit the golem for", atkdmg)

        elif move == "2":
            heal = random.randint(4, 8)
            playerh = playerh + heal
            print("You healed for", heal)

        else:
            print("You did nothing")

        if golemhealth > 0:
            goldmg = random.randint(4, 9)
            playerh = playerh - goldmg
            print("The golem smacks you for", goldmg)

        time.sleep(2)

    if playerh > 0:
        print("You somehow managed to beat the golem")
        winmesg("You make it out of the volcano covered in rock bits.")
    elif "wooden spear" in inventory:
            print ("the golem attempted to kill you, you pulled your spear out to keep the fight going")
    else:
        die("The golem crushes you")
       


