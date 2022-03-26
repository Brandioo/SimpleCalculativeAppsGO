word = "BANANA"
k=0
s=0

subs=[]

for i in range(len(word)):
    for j in range(len(word)):
        sub = word[i:j+1]
        if len(sub)>0:
            subs.append(sub)

# print(subs)


for i in range(len(word)):
    print(word[0:i+1])