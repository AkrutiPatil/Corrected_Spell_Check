# step-1 importing the required Library:
from spellchecker import SpellChecker


class SpellcheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()  # hello World['hello','world']
        corrected_words =[ ]

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_words}"')
                corrected_words.append(corrected_word)

        # step 4 - returning the corrected text
        return ''.join(corrected_words)

    def run(self):
        print("\n ____Spell Checker___")

        while True:
            text = input('Enter text to check (or type "exit" to quit):')

            if text.lower() == 'exit':
                print('Closing the program...')
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected text : {corrected_text}')


# step -6 running the main program:
if __name__ == "__main__":
    SpellcheckerApp().run()


