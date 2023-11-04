from Images import stages, logo
import os


class Hangman:
    stages = stages
    logo = logo
    current_stage = len(stages) - 1
    word_to_guess = ""
    letters_remaining = []
    letters_guessed = []
    game_over = False

    def __init__(self):
        os.system("cls")
        self._play_game()

    def _get_word(self):
        self.word_to_guess = input("Enter a word for other player to guess: ").casefold()
        self.letters_remaining = ["_"] * len(self.word_to_guess)

    def _progress_stage(self):
        self.current_stage -= 1

    def _print_current_stage(self):
        print(self.stages[self.current_stage])

    def print_current_status(self):
        # print("\n" * 100)
        print(" ".join(self.letters_remaining))
        print("letters guessed:", ", ".join(self.letters_guessed))
        self._print_current_stage()

    def _guess_letter(self):
        self.print_current_status()

        correct = False
        current_guess = input("Guess a letter: ").casefold()
        while len(current_guess) > 1 or current_guess in self.letters_guessed:
            current_guess = input("Please guess a single letter you have not guessed yet: ").casefold()

        for i in range(len(self.word_to_guess)):
            if self.word_to_guess[i] == current_guess:
                correct = True
                self.letters_remaining[i] = current_guess

        if not correct:
            self.letters_guessed.append(current_guess)
            self._progress_stage()

    def _check_win_lose(self):
        if "_" not in self.letters_remaining:
            print("You did it!")
            return True
        elif self.current_stage == 0:
            os.system("cls")
            self._print_current_stage()
            print("Sorry, you lose")
            return True

        return False

    def _play_game(self):
        print(logo)
        self._get_word()

        while not self.game_over:
            os.system("cls")
            self._guess_letter()
            self.game_over = self._check_win_lose()