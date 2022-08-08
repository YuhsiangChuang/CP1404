import string

def main():
    phrase= 'The cow jumped over the elephant'
    number_of_letter = count_letter(phrase)
    print(f'Number of letter: {number_of_letter}')

def count_letter(text):

    count =0
    for character in text:
        if character.lower() in string.ascii_letters:
            count+=1
    return count

main()