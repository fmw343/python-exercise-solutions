import random

lower_limit = 1000
upper_limit = 9999

def tracker():
    guesses = 0
    is_playing = True
    
    rando = [int(x) for x in str(random.randint(lower_limit, upper_limit))]
    
    while is_playing:
        user_input = int(input("Enter your guess: "))
        guesses += 1
        
        if user_input >= lower_limit and user_input <= upper_limit:
            user_input = [int(x) for x in str(user_input)]
            
            cows = 0
            bulls = 0
            
            for y in range(len(rando)):
                if user_input[y] == rando[y]:
                    cows += 1
                elif user_input[y] in rando:
                    bulls += 1
                    
            if user_input == rando:
                print(f"You guessed right using {guesses} tries!")
                
                user_input = input("Play again? (Y/N): ").lower()
                
                if user_input == "y":
                    tracker()
                else:
                    break
            else:
                print(f"{cows} cow" + ('s' if cows > 1 else '') + f", {bulls} bull" + ('s' if bulls > 1 else '') + ".")
            
        else:
            print(f"Stick to numbers between {lower_limit} and {upper_limit}!")

tracker()
