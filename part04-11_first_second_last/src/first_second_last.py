# Write your solution here
def first_word(param):
     words = param.split()
     return words[0] if len(words) > 0 else ""

def second_word(param):
     words = param.split()
     return words[1] if len(words) > 1 else ""

def last_word(param):
     words = param.split()
     return words[-1] if len(words) > 0 else ""

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))