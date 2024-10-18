print("Hint: camelCaseLooksLikeThis ")
variable = input("Please input a variable in camel case. ")

for i in variable:
    if i.isupper():
        print("_", i.lower(), end="")
    else:
        print(i, end="")
