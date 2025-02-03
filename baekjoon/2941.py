str = input()
croatian=["c=","c-","dz=","d-","lj","nj","s=","z="]

for cr in croatian:
    while(cr in str):
        i = str.find(cr)
        str = str.replace(cr,"*")
print(len(str))

