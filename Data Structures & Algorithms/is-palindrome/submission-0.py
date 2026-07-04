class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s).lower() # Convert the original string to lower case
        # Start from the end, go back to the beginning. Split to a list of strings
        split_string = s[::-1].split(" ")
        reversed_string = ''.join(split_string) # Convert back to a string in reverse
        reversed_string = re.sub(r"\W", "", reversed_string) # remove all non-alphanumeric characters
        return s == reversed_string