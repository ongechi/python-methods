#python string methods
#(i) isalpha() method - the method is used to return true attribute if the letters/characters used are alphabet letters
word = "Patrick"
k = word.isalpha()
r = word.isalpha()
print(r)
print(k)
#(ii) The index() method - finds the first occurrence of the specified value.
word = "Hello, welcome to my world."
x = word.index("e")
print(x)
#(iii) The expandtabs() method - sets the tab size to the specified number of whitespaces.
word = "H\te\tl\tl\to"
print(word)
print(word.expandtabs())
print(word.expandtabs(2))
print(word.expandtabs(4))
print(word.expandtabs(10))
#(iv) The center() method - it centers/aligns the string, using a specified character (space is default) as the fill character.
word = "banana"
a = word.center(20, "O")
print(x)
#(v)The casefold() method - returns a string where all the characters are lower case.
word = "Hello, And Welcome To My World!"
p = word.casefold() 
print(x)