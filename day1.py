x=input("enter your name:")
y=int(input("enter your age:"))
def greet(name):
    return f"Hello{name}!"
print(greet(x))
if y < 18:
    print("you are a minor")
else:
    print("you are an adult")
reversed_name=x[::-1]
print("your name reversed is:",reversed_name)