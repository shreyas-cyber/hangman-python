import random
def hangman():
    list_of_words=['peru','kittu','puttu','sheru','kairu']
    words=random.choice(list_of_words)
    turn=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')

    while len(words)>0:
        main_word=''
        for letter in words:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        if main_word==words:
            print(main_word)
            print("You Won",name,"!")
            break
        print('Guess the words:',main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print('Enter valid character')
            guess=input()
        if guess not in words:
            turn=turn-1
            if turn==9:
                print("Turns left 9")
                print("---------------")
            if turn==8:
                print("Turns left 8")
                print("---------------")
                print("       o       ")
            if turn==7:
                print("Turns left 7")
                print("---------------")
                print("       o       ")
                print("       |       ")
            if turn==6:
                print("Turns left 6")
                print("---------------")
                print("       o       ")
                print("       |       ")
                print("        \       ")
            if turn==5:
                print("Turns left 5")
                print("---------------")
                print("       o       ")
                print("       |       ")
                print("      / \       ")
            if turn==4:
                print("Turns left 4")
                print("---------------")
                print("      \o       ")
                print("       |       ")
                print("      / \       ")
            if turn==3:
                print("Turns left 3")
                print("---------------")
                print("      \o/       ")
                print("       |       ")
                print("      / \       ")
            if turn==2:
                print("Turns left 2")
                print("---------------")
                print("      \o/ |      ")
                print("       |       ")
                print("      / \       ")
            if turn==1:
                print("Turns left 1")
                print("---------------")
                print("      \o/__|      ")
                print("       |       ")
                print("      / \       ")
            if turn==0:
                print("You Lose",name,"!")
                print("---------------")
                print("       o__|      ")
                print("      /|\       ")
                print("      / \       ")
                break
name = input("Enter your name:")
print("Welcome", name)
print("------------------------------------------")
print("Try to guess word in less than 10 attempts")
hangman()

