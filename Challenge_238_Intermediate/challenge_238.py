import random

# Convert word into list of unique characters (char may only appear once)
# and generate score from that which will determine how often reoocurrences happen
def get_word_score(word):
    return len(list(set(word))) / len(word)
    
# Retrieves a random line of text from the password file using linecache.getline()
def get_password(difficulty):
    password_file = "enable1.txt"
    possible_passwords = [] # Array of possible passwords that match the criteria for the difficulty
    other_words = 0 # Amount of other words to go along side with  the password

    # Goes through each dictionary line to determine valid words based on dictionary
    # Could have done this and used predefined dictionaries but this is pretty fast
    with open(password_file) as f:
        for line in f:
            line = line.replace("\n", "")
            # Should be able to guess the word fairly easily within 4 tries
            if (difficulty == 1):
                other_words = 4
                if len(line) == 4:
                    possible_passwords.append(line)
            # Check for matching characters. If this is high, add to list for difficulty 2
            elif (difficulty == 2):
                other_words = 6
                if (len(line) <= 6 and len(line) >= 5 and get_word_score(line) <= 0.5):
                    possible_passwords.append(line)
            # Little bit more difficult
            elif (difficulty == 3):
                other_words = 8
                if (len(line) == 8 and (get_word_score(line) > 0.5 and get_word_score(line) <= 0.8)):
                    possible_passwords.append(line)
            # Pretty difficult
            elif (difficulty == 4):
                other_words = 10
                if (len(line) == 9 and (get_word_score(line) > 0.8 and get_word_score(line) <= 0.95)):
                    possible_passwords.append(line)
            # Quite hard
            elif (difficulty == 5):
                other_words = 15
                if (len(line) == 10 and (get_word_score(line) > 0.95)):
                    possible_passwords.append(line)

    # Retrieve random password possibilities
    password_list = []
    for x in range(other_words + 1):
        password_list.append(possible_passwords[random.randint(0, len(possible_passwords))].upper())
    return password_list

# Validates user input for validity                    
def get_difficulty():
    valid_input = False
    while not valid_input:
        dif = input("Difficulty (1-5)? ")
        if (int(dif) > 0 and int(dif) <= 5):
            valid_input = True
    return int(dif)

# Comparese two words and get's the amount of matched letters
def check_words(password, guess):
    count = 0
    counted = []
    for i in guess.upper():
        if (i in password and i not in counted):
            count += password.count(i)
            counted.append(i)
    print("") # Just to make it a bit tidier
    return count

# Container main game loop
def guess_game():
    difficulty = get_difficulty()
    
    # Get passwords and retrieve random password from array
    passwords = get_password(difficulty)
    password = passwords[random.randint(0, len(passwords) - 1)]
    password_len = len(password)
    
    game_over = False
    guesses_left = 4
    
    print(*passwords, sep="\n") # Output passwords
    while not game_over:
        guess = input("\nGuess ({0} left): ".format(guesses_left))
        
        result = check_words(password, guess)
        print("{0}/{1}".format(result, password_len))

        # Check if user has guessed correctly or if the user is out of guesses
        if (password == guess):
            print("Correct guess!")
            game_over = True
        guesses_left -= 1
        if (guesses_left <= 0):
            print("You have used all your guesses and failed to hack guess the password!")
            game_over = True  

if __name__ == "__main__":
    guess_game()
