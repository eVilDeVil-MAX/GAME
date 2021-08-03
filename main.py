import random

heal_uses = 0


# Hero Classes

class knight(object):
    health = 100
    strength = 15
    defence = 12
    magic = 1


class mage(object):
    health = 55
    strength = 4
    defence = 5
    magic = 18


class monk(object):
    health = 100
    strength = 12
    defence = 8
    magic = 4

    # tavern


def tavern_run():
    sword_upgrade_used = False
    print("Welcome to the tavern! im buck, if you need anything, ill be behind the bar")
    while True:
        selection = input("1. ask about new places to go \n2. Ask for a sword upgrade \n3. say thank you and leave")
        if selection == "1":
            print("I heard there is another tavern a while ahead")

        if selection == "2":
            print("Ive only got one, but here you go!")
            character.strength = character.strength + 2
            sword_upgrade_used = True

        if selection == "3":
            break


# Enemy Classes

class goblin(object):
    name = "Goblin"
    health = 30
    strength = 2
    defence = 2
    loot = random.randint(0, 2)


class bat(object):
    name = "Bat"
    health = 15
    strength = 1
    defence = 3
    loot = random.randint(0, 2)


class troll(object):
    name = "Troll"
    health = 40
    strength = 5
    defence = 1.5
    loot = random.randint(0, 2)


class tavern(object):
    name = "tavern"
    health = 1
    strength = 1
    defense = 1


class boss(object):
    name = "boss"
    health = 150
    strength = 50
    defence = 50


def gameOver(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        print("You have scored...", score)

        writeScore(score)

        file = open("score.txt", "r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()


def titleScreen():
    print("Select your choice!")
    selection = input("1. Continue \n2. New game \n3. Quit game \n")
    if selection == "1":
        with open('savefile.txt') as file:  # read the file
            contents = file.read()
        health, strength, defence, magic = contents.split(',')  # split it
        health = int(health)  # convert the strings into integers
        strength = int(strength)
        defence = int(defence)
        magic = int(magic)

    if selection == "2":
        score = 0
        heroselect()


def writeSave():
    with open("RpgGameSave.txt", "w") as file:
        file.write(str(character.health))
        file.write(",")
        file.write(str(character.strength))
        file.write(",")
        file.write(str(charater.defence))
        file.write(",")
        file.write(str(character.magic))


def writeScore(score):
    file = open("score.txt", "a")
    name = input("Type your name...")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def heroselect():
    print("Select your hero!")
    selection = input("1. Knight \n2. Mage \n3. Monk \n")
    if selection == "1":
        character = knight
        print("You have selected the Knight...These are their stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = mage
        print("You have selected the Mage...These are their stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = monk
        print("You have selected the Monk...These are their stats...")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()


def enemyselect():
    enemy = random.choices([goblin, bat, troll, tavern], weights=[10, 10, 10, 100])[0]
    return enemy


def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0, 2)
    lootDrop = loot[lootChance]
    return lootDrop


def lootEffect(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print("you drink the potion, increasing your health by 20!")
        print("Your health is now", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength + 2
        print("you swap your sword for the newer, much sharper one!")
        print("Your strength has been increased by 2")
        print("your new strength is now", character.strength)
        return character

    elif lootDrop == "shield":
        character.defence = character.defence + 2
        print("you swap your shield for the newer, much stronger one!")
        print("Your defence has been increased by 2")
        print("your new strength is now", character.defence)
        return character


def battlestate(score):
    global heal_uses
    enemy = enemyselect()
    if enemy == tavern:
        tavern_run()
        return
    print("a wild", enemy.name, "has appeared!")
    print("you have 3 options...")
    while enemy.health > 0:
        choice = input("1. Sword\n2. Magic \n3. RUN! \n4. Heal")

        if choice == "1":
            print("You swing your sword, attacking the", enemy.name)
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("You hit the enemy, their health is now....", enemy.health)
                critchance = random.randint(0, 20)
                if critchance > 2:
                    enemy.health = enemy.health - 10
                    print("You critical hit the enemy! their health is now", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)


                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10


                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score + 5


                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score + 15

                    print("You have defeated the", enemy.name)
                    print("looks like it dropped something!")
                    lootDrop = loot()
                    print("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "2":
            print("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0, 10)
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print("You hit the enemy, their health is now....", enemy.health)
                critchance = random.randint(0, 20)
                if critchance > 2:
                    enemy.health = enemy.health - 10
                    print("You critical hit the enemy! their health is now", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10


                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score + 5


                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score + 15

                    print("You have defeated the", enemy.name)
                    print("looks like it dropped something!")
                    lootDrop = loot()
                    print("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your spell fizzles and doesnt do damage!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "3":
            print("you try to run....")
            runchance = random.randint(1, 10)
            if runchance > 4:
                print("you got away unscratched!")
                break
            else:
                print("You try to run are caught by the monster")
                print("You try to defend but cannot, the enemy hits you for full damage...")
                character.health = character.health - enemy.strength
                print("Your health is now", character.health)
                gameOver(character, score)

        elif choice == "4":
            print("You try to heal")
            healchance = random.randint(1, 20)
            if healchance > 4 and character.magic == 18 and not heal_uses > 3:
                character.health + 15
                heal_uses += 1
            print("You healed yourself for 15 points!")
            if character.magic != 18:
                print("You didn't have a high enough magic skill!")
                break

        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("You have to pick 1, 2, 3, or 4!")


def BossBattleState(score):
    enemy = boss


titleScreen()

score = 0
character = heroselect()
while True:
    score = battlestate(score)
    writeSave()
    print(score)