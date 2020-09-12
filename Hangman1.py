import pymysql
from random import randint, choice

conn = pymysql.connect("127.0.0.1", user="root", passwd="password", db="Hangman", port=3306)
curr = conn.cursor()

class Hangman:

    def __init__(self, word, streak):
        self.word = word.lower()
        self.blank = ""
        self.count = 10
        self.letters_entered = []
        self.status = True
        self.hint = ''
        self.blank_array = []
        self.score_list = []
        self.streak = streak


    # Check if the given string is valid for multipalyer mode when the word is given by an opponent
    def string_validity(self):

        while len(self.word) < 6 or self.word.isalpha() == False:
            if len(self.word) < 6:
                self.word = input("Enter a word with at least 6 character: ")
            else:
                self.word = input("Enter a valid string: ")

        self.blank = "_ " * len(self.word)
        print(self.blank)
        return


    # Accept a single character from the user and check its validity
    def character_validity(self, letter):

        while letter.isalpha() == False or len(letter) != 1:
            if letter.lower() == "exit":
                return 'Exit'
            letter = input("Please enter a single alphabet: ")

        if letter in self.letters_entered:
            print("The alphabet was already guessed.")
            letter = self.character_validity('8')
        else:
            self.letters_entered.append(letter)

        return letter.lower()


    #Check for the presence of the letter in the string
    def letter_presence(self):

        while self.count > 0:
            if '_' in self.blank:
                print("Number of lives:", self.count)
                character = input("Enter a character:")
                valid_letter = self.character_validity(character)
                if valid_letter.lower() == 'exit':
                    print("Come back soon. Cya!")
                    return
                self.play(valid_letter, self.count)
            else:
                self.streak += 1
                print("Congratulations you won!")
                print("Your score for this game is:", self.score())
                return [self.score(), self.streak]
                break

            if (self.count == 4 and self.blank.count('_') > 1)  and self.status == True:
                self.need_clue()
                self.status = False

        if self.count == 0:
            self.streak = 0
            print("The word was:", self.word)
            print("Your score for this game is:", self.score())
            print("Better luck next time.")
            return [self.score(), self.streak]


    #Play each letter as the player guesses
    def play(self,valid_letter,count):
        if valid_letter in self.word:
            indices = []
            for i in range(0,len(self.word)):
                if self.word[i] == valid_letter:
                    indices.append(i)

            self.blank_array = self.blank.split(' ')

            for j in indices:
                self.blank_array[j] = valid_letter
            self.blank = ' '.join([str(elements) for elements in self.blank_array])
            print(self.blank)
        else:
            self.count = self.count-1
            print("Remaining number of lives: ", self.count)
            print(self.blank)


    #Option to get a clue
    def need_clue(self):
        self.hint = input("Do you need a clue?(Y/N): ")

        if self.hint == 'Y' or self.hint == 'y':
            while True:
                number = randint(0, len(self.word) - 1)

                if self.blank_array[number] == '_':
                    letter_clue = self.word[number]
                    indices = []

                    for i in range(0, len(self.word)):
                        if self.word[i] == letter_clue:
                            indices.append(i)

                    if len(indices) > 1:
                        print(len(indices), "characters are the same.")
                    else:
                        print("One of the characters is:", letter_clue)
                    break

                else:
                    continue

    def score(self):
        if self.hint == 'Y' or self.hint == 'y':
            score = self.count*10 - 5
        else:
            score = self.count*10
        return score



query = "Select * from Easy"
curr.execute(query)
results1 = list(curr.fetchall())

query2 = "Select * from Hard"
curr.execute(query2)
results2 = list(curr.fetchall())

word_selected = ""
score_list = []
Want_to_Play = 'Y'
words_used = []
streak = 0

while(Want_to_Play.upper() == 'Y'):

    if streak < 2: results = results1
    else: results = results2

    while len(word_selected) < 6 or (word_selected in words_used) or word_selected.find('-') != -1:
         word_selected = choice(results)[1]
    words_used.append(word_selected)

    test = Hangman(word_selected, streak)
    test.string_validity()

    [score_l, streak] = test.letter_presence()
    score_list.append(score_l)
    print("Total Score:", sum(score_list))
    Want_to_Play = input("Do you want to play again?(Y/N): ")


    if streak < 5: results = results1
    else: results = results2


















