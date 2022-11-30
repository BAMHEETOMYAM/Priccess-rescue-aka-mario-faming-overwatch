title = '''===============Welcome to Princess Rescue===============
Task  : Rescue the princess from the Dark Elves in the far far away forest where no one dare to challenge
Story : We will need a mighty hero who will help us defeat the dark side now please Enter your name
=========================================================='''
print(title)

user = input(": ")

print("==========================================================\n"
    "Welcome",user ,"There will be alot of preparation before challenge the Dark elves")
print("Please select your class before we start each class will contain different stats ")
print("1 : Warrior\n"
      "2 : Assasin\n"
      "3 : Mage\n"
      "4 : Berserker\n"
      "Please select your class before start by typing a number\n"
      "==========================================================")

classselectlst = ['1','2','3','4']



classselect = input(": ")



#Player stat
playerlevel = 0
playerexp = 0
health = 0
mana = 0
attack = 0
specialattk = 0
userclass = 'none'



# Error catch
while classselect not in classselectlst:
    print("try again!\n"
          "==========================================================")
    classselect = input(": ")
    if classselect in classselectlst:
        break

#Playerselectclass
def playerselectclass():

    #Player class stat
    if classselect == "1":
        health = 10
        mana = 3
        attack = 8
        specialattk = 9
        userclass = "Warrior"
        return health,mana,attack,specialattk,userclass
    elif classselect == "2":
        health = 8
        mana = 8
        attack = 5
        specialattk = 5
        userclass = "Assasin"
        return health, mana, attack, specialattk, userclass
    elif classselect == "3":
        health = 8
        mana = 12
        attack = 8
        specialattk = 7
        userclass = "Mage"
        return health, mana, attack, specialattk, userclass
    elif classselect == "4":
        health = 15
        mana = 5
        attack = 10
        specialattk = 8
        userclass = "Berserker"
        return health, mana, attack, specialattk, userclass

health, mana, attack, specialattk, userclass = playerselectclass()


#call player stat function when player exp hit certain playerexp
def playerstats():
    #Warrior class lv 1-10
    if userclass == "Warrior":
        if playerexp > 900:
            playerlevel = 10
            health = 110
            mana = 33
            attack = 88
            specialattk = 99
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 100
            mana = 30
            attack = 80
            specialattk = 90
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 90
            mana = 27
            attack = 72
            specialattk = 81
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 80
            mana = 24
            attack = 64
            specialattk = 72
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 70
            mana = 21
            attack = 56
            specialattk = 63
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 60
            mana = 18
            attack = 48
            specialattk = 54
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 50
            mana = 15
            attack = 40
            specialattk = 45
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 40
            mana = 12
            attack = 32
            specialattk = 36
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 30
            mana = 9
            attack = 24
            specialattk = 27
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 20
            mana = 6
            attack = 16
            specialattk = 18
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 10
            mana = 3
            attack = 8
            specialattk = 9
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Assasin":
        if playerexp > 900:
            playerlevel = 10
            health = 88
            mana = 88
            attack = 55
            specialattk = 55
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 80
            mana = 80
            attack = 50
            specialattk = 50
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 72
            mana = 72
            attack = 45
            specialattk = 45
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 64
            mana = 64
            attack = 40
            specialattk = 40
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 56
            mana = 56
            attack = 35
            specialattk = 35
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 48
            mana = 48
            attack = 30
            specialattk = 30
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 40
            mana = 40
            attack = 25
            specialattk = 25
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 32
            mana = 32
            attack = 20
            specialattk = 20
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 24
            mana = 24
            attack = 15
            specialattk = 15
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 16
            mana = 16
            attack = 10
            specialattk = 10
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 8
            mana = 8
            attack = 5
            specialattk = 5
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Mage":
        if playerexp > 900:
            playerlevel = 10
            health = 88
            mana = 132
            attack = 88
            specialattk = 77
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 80
            mana = 120
            attack = 80
            specialattk = 70
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 72
            mana = 108
            attack = 72
            specialattk = 63
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 64
            mana = 96
            attack = 64
            specialattk = 56
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 56
            mana = 84
            attack = 56
            specialattk = 49
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 48
            mana = 72
            attack = 48
            specialattk = 42
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 40
            mana = 60
            attack = 40
            specialattk = 35
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 32
            mana = 48
            attack = 32
            specialattk = 28
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 24
            mana = 36
            attack = 24
            specialattk = 21
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 16
            mana = 24
            attack = 16
            specialattk = 14
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 8
            mana = 12
            attack = 8
            specialattk = 7
            return playerlevel,health,mana,attack,specialattk
    elif userclass == "Berserker":
        if playerexp > 900:
            playerlevel = 10
            health = 175
            mana = 55
            attack = 110
            specialattk = 88
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 800:
            playerlevel = 9
            health = 150
            mana = 50
            attack = 100
            specialattk = 80
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 700:
            playerlevel = 8
            health = 135
            mana = 45
            attack = 90
            specialattk = 72
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 600:
            playerlevel = 7
            health = 120
            mana = 40
            attack = 80
            specialattk = 64
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 500:
            playerlevel = 6
            health = 105
            mana = 35
            attack = 70
            specialattk = 56
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 400:
            playerlevel = 5
            health = 90
            mana = 30
            attack = 60
            specialattk = 48
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 300:
            playerlevel = 4
            health = 75
            mana = 25
            attack = 50
            specialattk = 40
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 200:
            playerlevel = 3
            health = 60
            mana = 20
            attack = 40
            specialattk = 32
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 100:
            playerlevel = 2
            health = 45
            mana = 15
            attack = 30
            specialattk = 24
            return playerlevel,health,mana,attack,specialattk
        elif playerexp >= 50:
            playerlevel = 1
            health = 30
            mana = 10
            attack = 20
            specialattk = 16
            return playerlevel,health,mana,attack,specialattk
        elif playerexp > -1:
            playerlevel = 0
            health = 15
            mana = 5
            attack = 10
            specialattk = 8
            return playerlevel,health,mana,attack,specialattk











playerlevel,health,mana,attack,specialattk = playerstats()



print("Welcome again", user ,"The",userclass)
print("There will be a ton of monster in this world you will need to preapare your self before fight them \n"
"You can choose world you gonna play first there will be 2 different world\n"
"1 : FarmWorld(Where you can farm your level)\n"
"2 : CampaignWorld(Where you can go defeat DarkElves and rescue princess)\n"
      "==========================================================")

worldselect = input("Select your world by number: ")

#Farmworld
worldlevel = 0
slimehealth = 20
Werewolf = 40
Troll = 100



