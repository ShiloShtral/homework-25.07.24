mahrozet = " fun-day   "
print(mahrozet.strip())

print("hello".isalpha())

print("777".isdigit())

print("    ".isspace())

joinlist: str = ["N", "I", "N", "J", "A"]
print("".join(joinlist))

print("*".join(joinlist))

Mahrozet2 = "hELLO"
find = "e"

if find.lower() in Mahrozet2.lower():
    print("True")
else:
    print("False")

complist = input("Type in a word and digits : ")

uppercomplist = [char.upper() for  char in complist if char.isalpha()]
print(uppercomplist)



