from sys import argv
 greeted_name =argv
 greeted_name = argv[1]

def greet( greeted_name: str):     
 return f"Hello, { greeted_name}!"
name1=greet( greeted_name)
print (name1)
