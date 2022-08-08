def main():

    phrase = input('Enter a phrase to find number of vowels: ')

    vowel_count = 0
    for char in phrase:
        if char in 'AEIOUaeiou':
            vowel_count+=1

    print(f'The phrase has {vowel_count} vowels.')

main()