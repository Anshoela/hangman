import random
def hangman():
    word = random.choice(["ironman","hulk","thor","captainamerica","clint","loki","avengers","nick","phil","maria","vishal","tomboy","rich","meghan","skrrtskrrt","drama","valorant","dragonballz" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    print("It is a ",len(word),"letter word")
    turns=10
    guessmade = ''

    while len(word)>0:
        main=""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main+"_" +" "
        if main ==word:
            print(main)
            print("YOU WIN!!!!!!! DYWWAGDYGCHCHABDHSAD CONGRATULATIONSSSSS!!!! ")
            break
        print ("Guess the word :",main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
            print(guessmade)
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word :
            turns = turns - 1
            if turns == 9:
                print("9 turns left UMMMMMKAY NT")
                print("  ----------------  ")
            if turns == 8:
                print("8 turns left GOOD TRY")
                print("  ----------------  ")
                print("           O         ")
            if turns == 7:
                print("7 turns left KEEP TRYING")
                print("  ----------------  ")
                print("           O         ")
                print("           |        ")
            if turns == 6:
                print("6 turns left BRUHHHHHHHH")
                print("  ----------------  ")
                print("           O         ")
                print("           |        ")
                print("          /        ")
            if turns == 5:
                print("5 turns left YOU'RE LOSING ME PATHOLOGICAL PEOPLE PLEASER")
                print("  ----------------  ")
                print("           O         ")
                print("           |        ")
                print("          / \       ")
            if turns == 4:
                print("4 turns left DDU DDU 뚜두뚜두 ")
                print("  ----------------  ")
                print("         \ O         ")
                print("           |        ")
                print("          / \       ")
            if turns == 3:
                print("3 turns left WHAT U GONNA DO WHEN I COME WITH GUN HEHEHEHE ")
                print("  ----------------  ")
                print("         \ O / ")
                print("           |        ")
                print("          / \       ")
            if turns == 2:
                print("2 turns left YOUR PLAYER IS SOOOOO DEDDDDD ")
                print("  ----------------  ")
                print("         \ O / |       ")
                print("           |        ")
                print("          / \       ")
            if turns == 1:
                print("1 turns left REMEBER ITS NOT A RACE EVERONE GOT THESE DAYS ")
                print("Last breaths counting, Take care!")
                print("  ----------------  ")
                print("         \ O / _|      ")
                print("           |        ")
                print("          / \       ")
            if turns == 0:
                print(" ADWQJHWQABXSJAWBDH YOU LLLLLOOOOOOSSSSSSTTTTTTTTTTT GG ")
                print("YOU LET A KIND MAN DIE -_-")
                print("  ----------------  ")
                print("           O_|       ")
                print("         / | \     ")
                print("         /   \     ")
                print(" The word was : "+word) 
                break
name= input("Enter your name")
print("Hellewwww thereeeee",name)
print("-----------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
                
                
                
                
                
            
                
