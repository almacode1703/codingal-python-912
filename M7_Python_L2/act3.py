# String Oprations

first_name = "John"
print("First Name:", first_name)

last_name = "Doe"   
print("Last Name:", last_name)

full_name = first_name + " " + last_name
print("Full Name:", full_name)

example = "Happy"*5;
print("Repeated String:", example)


word = "coding"
# Length
length = len(word)
print("Length of the word '{}': {}".format(word, length))

# Accessing Characters
first_char = word[0]
print("First character of '{}': {}".format(word, first_char))

last_char = word[-1]
print("Last character of '{}': {}".format(word, last_char))

# Slicing
substring = word[1:4]
print("Substring of '{}' from index 1 to 3: {}".format(word, substring))    

# Convert to Uppercase
uppercase_word = word.upper()
print("Uppercase of '{}': {}".format(word, uppercase_word))