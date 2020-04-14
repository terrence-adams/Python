class Input:
    empty_word = ""

    def __init__(self):
        Input.empty_word = "I am not empty any more."

    def my_string_input(self, str1='My words.'):
        word = str1
        word2 = "L0RD"
        print(word)
        print("This string is all alpha characters:", word2.isalpha())
        print(word.upper())
        print(word.lower())


if __name__ == "__main__":
    my_input = Input()
    my_input.my_string_input("Hello , my new world.")
