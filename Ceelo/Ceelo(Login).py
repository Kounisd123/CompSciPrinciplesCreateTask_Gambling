import random
import time

quit = 0
pstrength = 2
cstrength = 2
credits = 0
bet = 0
uname = ''
pword = ''
uname_file = '/Users/dimitrioskounis/Desktop/CompSciCreateTask/CompSciPrinciplesCreateTask_Gambling/Ceelo/usernames.txt'
pword_file = '/Users/dimitrioskounis/Desktop/CompSciCreateTask/CompSciPrinciplesCreateTask_Gambling/Ceelo/passwords.txt'
credits_file = '/Users/dimitrioskounis/Desktop/CompSciCreateTask/CompSciPrinciplesCreateTask_Gambling/Ceelo/credits.txt'
logged_in = False
i = 0
starting_credits = 0

#By Jay
class Dice:
    def __init__(self,max_pips):
        assert len(max_pips) >= 1, 'Dice.__init__: max_pips is empty'
        for i in range(0,len(max_pips)):
            p = max_pips[i]
            assert p >= 1, 'Dice.__init__: max_pips['+str(i)+']='+str(p)+': must be an int >= 1'
        self._max_pips   = max_pips[:]
        self._pips      = [0]*len(max_pips)
        self._roll_count = 0

    def roll(self):
        self._roll_count
        self._pips = [ random.randint(1,max_pips) for max_pips in self._max_pips ]
        return self

    def rolls(self):
        return self._roll_count

    def all_pips(self):
        return self._pips[:]

    def pip_sum(self):
        return sum(self._pips)

#By Dimitri
def cash_out(path, value):
    global i
    with open(path, 'r') as file:
        saved_credits = file.read().split('\n')
        saved_credits[i] = value
    with open(path, 'w') as file:
        for balance in saved_credits:
            if balance != "":
                file.write(str(balance) + "\n")

#By Dimitri
def login():
    global uname
    global pword
    global credits_file
    global uname_file
    global pword_file
    global logged_in
    global credits
    global i
    global starting_credits
    uname = str(input("Enter your username: ").lower())
    pword = str(input("Enter your password: "))
    print("")
    current_unames = []
    current_pword = []
    saved_credits = []
    with open(uname_file) as uname_database:
        users = uname_database.read()
        current_unames = users.split()
    with open(pword_file) as pword_database:
        pwords = pword_database.read()
        current_pword = pwords.split()
    with open(credits_file) as credits_database:
        creds = credits_database.read()
        saved_credits = creds.split()
    if uname in current_unames:
        i = current_unames.index(uname)
        if pword == current_pword[i]:
            credits = int(saved_credits[i])
            starting_credits = credits
            print("")
            print("You have successfully logged in as " + uname + ".")
            print("")
            time.sleep(1)
            print("Here are 100 credits for logging in!")
            print("")
            credits = credits + 100
            time.sleep(1)
            print("You have " + str(credits) + " credits remaining.")
            print("")
            logged_in = True
        else:
            print("")
            print("Access denied.")
            print("")
    else:
        print("")
        print("Access denied.")
        print("")

#ByDimitiri
def create_user():
    global uname
    global pword
    global uname_file
    global pword_file
    global credits_file
    print("")
    print("Create User")
    print("")
    uname = str(input("Enter new username: ").lower())
    pword = str(input("Enter new password: "))
    print("")
    current_unames = []
    with open(uname_file) as uname_database:
        users = uname_database.read()
        current_unames = users.split()
    if uname in current_unames:
        print('That user already exists!')
        print("")
    else:
        with open(uname_file, 'a') as uname_database:
            uname_database.write(uname + "\n")
        with open(pword_file, 'a') as pword_database:
            pword_database.write(pword + "\n")
        with open(credits_file, 'a') as credits_database:
            credits_database.write("1000\n")
        print("You successfully made the user: " + uname)

#By both Dimitri and Jay
def login_phase():
    global logged_in
    while logged_in == False:
        print("")
        lchoice = str(input("(c)reate new user\n(l)ogin as existing user\n------------------------\n").lower())
        if lchoice == "c":
            create_user()
        elif lchoice == "l":
                login()
        else:
            print("")
            print("I don't understand.")

#By Jay
def betting_phase():
    global credits
    global bet
    bet_placed = 0
    while bet_placed == 0:
        bet = int(input("How much would you like to bet?\n"))
        print("")
        time.sleep(0.75)
        if credits < bet:
            print("You can't bet more credits than you have!")
            print("")
        if bet < 0:
            print("You must enter a positive number.")
            print("")
        if credits >= bet and bet > 0:
            credits = credits - bet
            if bet == 0:
                print("We will just play for fun then.")
                print("")
            print("You have " + str(credits) + " credits remaining.")
            print("")
            bet_placed = 1

#By Jay
def prolling_phase():
    global pstrength
    pstrength = 2
    r = 0
    while r < 5 and pstrength == 2:
        input("Press [Enter] to roll the dice!\n")
        d.roll()
        r = r + 1
        play = d.all_pips()
        time.sleep(0.25)
        print(play)
        time.sleep(0.25)
        print("")
        play.sort()
        pstrength = 2
        if play[0] == 1 and play[1] == 2 and play[2] == 3:
            pstrength = 1
        if play[0] == 4 and play[1] == 5 and play[2] == 6:
            pstrength = 15
        if play[0] == play [1] or play[1] == play[2]:
            if play[0] == play[1]:
                pstrength = play[2] + 2
            if play[1] == play[2]:
                pstrength = play[0] + 2
            if play[0] == play[1] == play[2]:
                pstrength = int(int(d.pip_sum()) / 3) + 8
        if pstrength == 1:
            print("Ouch! You lose. Better luck next time!")
        if 3 <= pstrength <= 8:
            value = pstrength - 2
            print("You rolled a " + str(value) + "! Let's see how it holds up.")
        if 9 <= pstrength <= 14:
            value = pstrength - 8
            print("You rolled triple " + str(value) + "s! Let's see how it holds up.")
        if pstrength == 15:
            print("Congrats! You win!")
        if pstrength == 2 and r < 5:
            print("Roll again please.")
        if pstrength == 2 and r >= 5:
            print("Ouch! You rolled out!")
        print("")
        time.sleep(0.25)

#By Dimtiri
def crolling_phase():
    global cstrength
    cstrength = 2
    r = 0
    while r < 5 and cstrength == 2:
        d.roll()
        r = r + 1
        play = d.all_pips()
        time.sleep(0.75)
        print(play)
        time.sleep(0.75)
        print("")
        play.sort()
        cstrength = 2
        if play[0] == 1 and play[1] == 2 and play[2] == 3:
            cstrength = 1
        if play[0] == 4 and play[1] == 5 and play[2] == 6:
            cstrength = 15
        if play[0] == play [1] or play[1] == play[2]:
            if play[0] == play[1]:
                cstrength = play[2] + 2
            if play[1] == play[2]:
                cstrength = play[0] + 2
            if play[0] == play[1] == play[2]:
                cstrength = int(int(d.pip_sum()) / 3) + 8
        if cstrength == 1:
            print("Congrats! You win!")
        if 3 <= cstrength <= 8:
            value = cstrength - 2
            print("I rolled a " + str(value) + "! Let's see how it holds up.")
        if 9 <= cstrength <= 14:
            value = cstrength - 8
            print("I rolled triple " + str(value) + "s! Let's see how it holds up.")
        if cstrength == 15:
            print("Sorry! I win!")
        if cstrength == 2 and r < 5:
            print("Let me roll again.")
        if cstrength == 2 and r >= 5:
            print("Ouch! I rolled out!")
        print("")
        time.sleep(.75)

#By Jay
def play_again():
    global quit
    global pstrength
    global cstrength
    global credits
    global bet
    quit = 0
    if int(pstrength) > int(cstrength):
        print("Looks like you won.")
        print("")
        time.sleep(0.75)
        print("You won " + str(bet) + " credits.")
        print("")
        time.sleep(0.75)
        credits = credits + (bet * 2)
        time.sleep(0.75)
    if int(cstrength) > int(pstrength):
        print("Looks like I won.")
        print("")
        time.sleep(0.75)
    if int(pstrength) == int(cstrength):
        print("Looks like we tied.")
        print("")
        credits = credits + bet
        time.sleep(0.75)
    print("You currently have " + str(credits) + " credits.")
    print("")
    time.sleep(0.75)
    while quit != 1 and quit != 2 :



        print ("Exiting the program without typing N will lose your progress.")
        again = str(input("Would you like to play again? [Y/N]"))
        print("")
        if again == 'N' or again == 'n':
            cash_out(credits_file, credits)
            quit = 1
            break
        elif again == 'Y' or again == 'y':
            quit = 2
            betting_phase()
            break
        else:
            print("Sorry but I don't understand. Please use [Y] for yes and [N] for no.")
            print("")

#By both Dimtitri and Jay
def game():
    global pstrength
    global cstrength
    global d
    d = Dice([6,6,6])
    while quit != 1:
        print("Your turn!")
        print("")
        prolling_phase()
        if pstrength != 1 and pstrength != 15:
            time.sleep(0.5)
            print("My turn!")
            print("")
            crolling_phase()
        play_again()

#By Jay
def main():
    login_phase()
    betting_phase()
    game()

#By Jay
print("Welcome to Ceelo!")
instructions = str(input("To see instructions on how to play please press [I]. Otherwise, press [Enter].\n"))
while instructions == 'I' or instructions == 'i':
    print("")
    print("Ceelo is a game played with 3 dice.")
    time.sleep(1)
    print("You get 5 rolls to score and once you score your turn ends.")
    time.sleep(1)
    print("In order to score, you must roll doubles, triples, [1, 2, 3], or [4, 5, 6]")
    time.sleep(1)
    print("[1, 2, 3] results in an automatic loss and [4, 5, 6] results in an automatic win.")
    time.sleep(1)
    print("If you roll doubles, your score is the leftover number.")
    time.sleep(1)
    print("Triples beats doubles, and higher triples beats a lower triple.")
    time.sleep(1)
    print("|---------------------|")
    print("|    Scoring Table    |")
    print("|---------------------|")
    print("| 1, 2, 3 |   Lose    |")
    print("|---------|-----------|")
    print("| x, y, z | No Score  |")
    print("|---------|-----------|")
    print("| x, x, 1 |     1     |")
    print("|---------|-----------|")
    print("| x, x, 2 |     2     |")
    print("|---------|-----------|")
    print("| x, x, 3 |     3     |")
    print("|---------|-----------|")
    print("| x, x, 4 |     4     |")
    print("|---------|-----------|")
    print("| x, x, 5 |     5     |")
    print("|---------|-----------|")
    print("| x, x, 6 |     6     |")
    print("|---------|-----------|")
    print("| 1, 1, 1 |     7     |")
    print("|---------|-----------|")
    print("| 2, 2, 2 |     8     |")
    print("|---------|-----------|")
    print("| 3, 3, 3 |     9     |")
    print("|---------|-----------|")
    print("| 4, 4, 4 |    10     |")
    print("|---------|-----------|")
    print("| 5, 5, 5 |    11     |")
    print("|---------|-----------|")
    print("| 6, 6, 6 |    12     |")
    print("|---------|-----------|")
    print("| 4, 5, 6 |    Win    |")
    print("|---------------------|")
    time.sleep(1)
    instructions = str(input("To see these instructions again, press [I]. To continue, press [Enter]."))
main()
