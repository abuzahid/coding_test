#Getting user input
string_input = input("Please enter the string to test palindrome: ")

#Checking palindrome number
def check_palindrome(string_input):
    # If user input is not empty
    if string_input:
        # Reversing the input string and checking if that is same as the input string or not
        if string_input==string_input[::-1]:
            return True
        else:
            return False
    # If user input is empty
    else:
        return False

#Calling the palindrome checking function to get output
print(check_palindrome(string_input))
