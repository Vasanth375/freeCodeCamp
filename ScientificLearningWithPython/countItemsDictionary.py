names = ['tony', 'banner', 'steven', 'tony', 'stark', 'stark']
name = dict()

# counting the number of items from dictionary
for i in names:
    if i not in name:
        name[i] = 1
    else:
        name[i] = name[i] + 1

# the get method used to return the key using the value if the key not exist in the dict returns None or default value providing in the
# method of passing argument
print(name.get('tonyvn', 'not Exist'))
# -----------------------------------------------------------------------------------------------------------------------------------------
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)