# QuantbitTask
#Task 1 Reverse a string without using built-in methods.
#Input: "hello"
#Output: "olleh"
#Task1 Code:

def rev_str(s):
        reversed_string=""
        for char in s:
                  reversed_string = char + reversed_string
        return reversed_string
input_string="hello"
output_string = rev_str(input_string)
print("reversed string :", output_string)
