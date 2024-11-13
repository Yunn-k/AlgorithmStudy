str = input()
result = ''

for i in str:
    if(i.isupper() == True):
        result += i.lower()
    else :
        result += i.upper()

print(result)
#print(str.swapcase()) 로도 가능