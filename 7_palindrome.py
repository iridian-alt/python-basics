def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    invert_word = word[::-1]
    if word == invert_word:
        return True
    else:
        return False




def run():
    word = input('Write a word: ')
    es_palindromo = palindromo(word)
    if es_palindromo == True:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')




if __name__ == '__main__': #We are telling what function we want to run first
    run()
 