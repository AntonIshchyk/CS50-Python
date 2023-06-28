def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter a sentence or phrase: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)
main()