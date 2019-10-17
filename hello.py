from sys import argv
name=argv
name = argv[1]

def greet(name: str):     
 return f"Hello, {name}!"
name1=greet(name)
print (name1)