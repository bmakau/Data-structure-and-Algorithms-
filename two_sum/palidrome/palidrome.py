class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Checks if the input is less than zero
        #negative numbers are not palindrome
        if x < 0:
            return False
       #creates variable to hold the original value of input and reverse
        original = x
        reverse = 0
        #121
        #condition checks if the number is less than 0 
        while x > 0:
            rem = x % 10 #extracts the last digit 
            reverse *=10 
            reverse += rem
            x //= 10
        return original == reverse