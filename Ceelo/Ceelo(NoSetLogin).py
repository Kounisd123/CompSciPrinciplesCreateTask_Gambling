import random
import time


quit = 0
pstrength = 2
cstrength = 2
credits = 1000
bet = 0


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
        self._roll_count += 1
        self._pips = [ random.randint(1,max_pips) for max_pips in self._max_pips ]
        return self


    def number_of_dice(self):
        return len(self._pips)


    def all_pip_maximums(self):
        return self._max_pips[:]


    def rolls(self):
        return self._roll_count


    def pips_on(self,i):
        assert self._roll_count > 0, 'Dice.pips_on: dice not rolled'
        assert 0<= i < len(self._pips), \
          'Dice.pips: die index i('+str(i)+') must be >= 0 and <'+str(len(self._pips))
        return self._pips[i]


    def all_pips(self):
        return self._pips[:]


    def pip_sum(self):
        assert self._roll_count > 0, 'Dice.pip_sum: dice not rolled'
        return sum(self._pips)


    def pips_same(self):
        return all( [self._pips[0] == p for p in self._pips] )


    def __str__(self):
        return 'Dice('+str(self._pips)+')'


    def __repr__(self):
        return 'Dice('+str(self._max_pips)+')'


    def standard_rolls_for_debugging(self):
        random.seed(5121022)

class Player:
    def logon(self):
        global uname
        global pword
        global creds
        global credits
        uname_input = str(input("Please enter your username."))
        print("")
        pword_input = str(input("Please enter your password."))
        print("")
        if uname_input in uname and pword_input in pword:
            print("Access granted.")
            global credits
            user_index = uname.index(uname_input)
            credits = creds[user_index]
            print("You have " + str(credits) + " credits.")
        else:
            print("Access denied.")

def betting_phase():
    global credits
    global bet
    bet_placed = 0
    while bet_placed == 0:
        bet = int(input("How much would you like to bet?"))
        print("")
        time.sleep(0.75)
        if credits >= bet:
            credits = credits - bet
            print("You have " + str(credits) + " credits remaining.")
            print("")
            bet_placed = 1
        elif credits < bet:
            print("You can't bet more credits than you have!")
            print("")
        else:
            print("I don't understand...")
            print("")

def prolling_phase():
    global pstrength
    pstrength = 2
    r = 0
    while r < 5 and pstrength == 2:
        d.roll()
        r = r + 1
        play = d.all_pips()
        time.sleep(0.75)
        print(play)
        time.sleep(0.75)
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
        time.sleep(0.75)

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
        again = str(input("Would you like to play again? [Y/N]"))
        print("")
        if again == 'N' or again == 'n':
            quit = 1
            break
        elif again == 'Y' or again == 'y':
            quit = 2
            betting_phase()
            break
        else:
            print("Sorry but I don't understand. Please use [Y] for yes and [N] for no.")
            print("")

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
            print("My turn!")
            print("")
            crolling_phase()
        play_again()

def main():
    betting_phase()
    game()

main()
