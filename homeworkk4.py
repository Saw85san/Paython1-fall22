








English = open("C:/Users/TOSHIBA/Downloads/english_dictionary.txt", "r")

line = English.readline()

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
for line in open("C:/Users/TOSHIBA/Downloads/english_dictionary.txt"):

    if (line == '\n'):
        continue
    line = line.split('(')
    word = line[0].strip()
    line[1] = line[1].split(')')
    line[1][1] = line[1][1].strip()
    meanings = line[1][1].split('; ')
    
    pos = line[1][0]
    wms = [word, meanings]

    if pos in dict1.keys():
        dict1[pos].append(wms)
    else :
        dict1[pos]=[]
        dict1[pos].append(wms)

#from here the dictionary is ready for you to play with 
print("\nSuffix of nouns : \n")
for item in dict1['n.']:
    word = item[0]
    if (len(word)>3):
        suffix = word[-4:]
        if suffix in dict2.keys():
            dict2[suffix] += 1
        else :
            dict2[suffix] = 1

sorted_dict = {}
sorted_keys = sorted(dict2, key=dict2.get, reverse=True)  # [1, 3, 2]

for f in sorted_keys:
    sorted_dict[f] = dict2[f]

count=0
for i in sorted_dict.keys() :
    print(i, " : ", sorted_dict[i])
    count += 1
    if (count == 10): break



print("\n..............................\n")
print("Suffix of verbs :\n ")
for item in dict1['v.']:

    word = item[0]
    if (len(word)>3):
        suffix = word[-4:]
        if suffix in dict3.keys():
            dict3[suffix] += 1
        else :
            dict3[suffix] = 1

sorted_dict = {}
sorted_keys = sorted(dict3, key=dict3.get, reverse=True)  # [1, 3, 2]

for f in sorted_keys:
    sorted_dict[f] = dict3[f]

count=0
for i in sorted_dict.keys() :
    print(i, " : ", sorted_dict[i])
    count += 1
    if (count == 10): break



print("\n...............................\n")


print("Suffix of adjectve :\n ")
for item in dict1['a.']:
   
     word = item[0]  
     if (len(word)>3):
       
        suffix = word[-4:]
        
        if suffix in dict4.keys():
            dict4[suffix] += 1
        else :
            dict4[suffix] = 1
        
       
sorted_dict = {}
sorted_keys = sorted(dict4, key=dict4.get, reverse=True)  # [1, 3, 2]

for f in sorted_keys:
    sorted_dict[f] = dict4[f]

count=0
for i in sorted_dict.keys() :
    print(i, " : ", sorted_dict[i])
    count += 1
    if (count == 10): break
