# keyword argument = an argument preceded by an identifier 
#                    helps with readability
#                    order of arguments does not matter

def greetings(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

greetings(last="Shaban", first="Muhammad", title="Mr.", greeting="Hello")
