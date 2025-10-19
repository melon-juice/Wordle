import random

print("""\nGuess the WORDLE in 6 tries!
Each guess  must be a valid 5-letter-word. Hit the enter button to sumbit.
\t  - not in the word in any spot
\t* - in the word but not in the right spot
\t🗸 - in the word and in the correct spot\n""")

def get_words():
    words=[]
    with open("five_letter_word_list.txt","r") as file:
        for line in file:
            line=line.replace("\n","")
            words.append(line)
        file.close()
    return words

def get_guess():
    print("Guess a word:")
    while True:
        try:
            user_input=(input(">  ").upper())
            guess=[*user_input]
            
            if len(guess)!=5:
                print("\tEnter a 5-letter word!")
                raise Exception
            
            for letter in guess:
                if letter.isupper()==False:
                    print("\tPlease only enter letters!")
                    raise Exception
                
            if user_input.lower() not in get_words():
                print("Word not in list.")
                print("Would you like to add this word to the list? (y/n)")
                add=""
                while add=="":
                    choice=input(">>>  ").lower()
                    if choice=="y":
                        add=True
                    elif choice=="n":
                        add=False
                    
                if add==True:
                    with open("five_letter_word_list.txt","a") as file:
                        file.write("\n"+user_input.lower())
                        print("Word successfully added to list.")
                        file.close()
                if add==False:
                    print("Word was not accepted")
                    raise Excpetion
            break
        
        except Exception:
            print("Try again:")
    return guess

def check_wordle(wordle):
    guess=get_guess()
    response=[]

    if guess==wordle:
        return guess,response
        
    for i in range(5):
        if guess[i]==wordle[i]:
            response.append("🗸")
        elif guess[i] in wordle:
            response.append("*")
        else:
            response.append(" ")
    #print(guess,response)
    return guess,response

################################# driver code #############################################

play_again="y"

while play_again=="y":

    ## sorts word list alphabetically

    words=get_words()
    words.sort()
    with open("five_letter_word_list.txt","w") as file:
        for word in words:
            file.write(word+"\n")
    #print(words)

    ## generates random wordle

    random_word=random.choice(get_words()).upper()
    wordle=[*random_word]
    #print(wordle)

    for i in range(6):
        guess,arr=check_wordle(wordle)
        if not arr:
            print("\n\tYes! You got it right!")
            break
        print("\t",guess[0],guess[1],guess[2],guess[3],guess[4])
        print("\t",arr[0],arr[1],arr[2],arr[3],arr[4])
        if i==5:
            print("\n\nYou ran out of turns!")
    print("The word was",random_word)

    print("\n\tPLAY AGAIN? (y/n)")
    play_again=""
    while play_again not in ("y","n"):
        play_again=input(">>>  ").lower()

print("Game has ended.")
x=input("Press [ENTER] to exit program")
quit()

    
        



    
