import random


class HangmanGame(object):

    words = ["guessing","apple","television","earphones",'mobile',
            "apple","macbook","python","sunset",'sunrise','winter',
            "opensource",'rainbow','computer','programming','science',  
             'python','datascience','mathematics','player','condition',  
             'reverse','water','river','boardmember']

    def start(self):
        name = input("Enter your name = ")
        print(f"Hello {name}! Welcome to the guessing game!")
        self.play()

    def play(self):
        chances = 10
        guesses = ""

        index = random.randint(0, len(self.words)-1)
        word = self.words[index]
        indexes = random.sample(range(0, len(word)), 3)

        for i in indexes:
            guesses += word[i]

        while chances > 0:
            won = True
            for ch in word:
                if ch in guesses:
                    print(ch, end=" ")
                else:
                    print("_", end=" ")
                    won = False

            if won:
                print("\nYou won!")
                print(f"Your score is {chances * 10})")
                self.playagain() #ask user want to play again
                break
                  
            # take a guess from the user 
            guess = input("\nGuess a character: ")
            guesses += guess
                
            if guess not in word:
                chances -= 1
                print("\nWrong Answer!!")
                print(f"\nYou have {chances} chances left!")
            
                if chances == 0:
                    print("You lose!!")
                    self.playagain() #ask user want to play again
                    break

    def playagain(self):

        play = input("Do you want to play again? (Yes/No): ")
        
        if play == "Yes":
            self.play()


if __name__ == '__main__':
    HangmanGame().start()