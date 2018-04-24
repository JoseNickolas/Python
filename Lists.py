fhandle = input('Enter file name:')
fhandle = open('romeo.txt','r')
lst = list()

for words in fhandle:
    words = words.strip()
    words = words.split()

    for element in words:
        if element in lst:
            continue
        else:
            lst.append(element)

lst.sort()
print(lst)
