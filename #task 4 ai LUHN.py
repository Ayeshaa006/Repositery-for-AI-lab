#task 4 
#1.luhn algorithm
def is_luhn_valid(card_no):
    digits = [int(d) for d in str(card_no)]
    checksum = digit.pop()
    digits.reverse()
    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total_sum = sum(digits) + checksum
    return total_sum % 10 == 0
#testing
test_card = "79927398713"
print(f"is the card valid? {is_luhn_valid(test_card)}")



#2.removing punctuations from a string
import string
def remove_punctuation(input_string):
    cleaned_string = ""
    for char in input_string:
        if char not in string.punctuation:
            cleaned_string += char
    return cleaned_string
#testing
sample_text = "hey! this is AI lab; let's code."
print(f"original: {sample_text}")
print(f"cleaned: {remove_punctuation(sample_text)}")




#3.sort sentence in alphabetic order
def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    return "".join(words)
#testing
my_sentence = "python is an amazing language for AI"
print(f"sorted: {sort_sentence(my_sentence)}")

