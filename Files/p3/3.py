from collections import Counter

with open('T:\\Programmes\\Python\\Data Science\\52_MCA_DataScience_Lab\\Files\p3\\freequency.txt') as f:
    print(Counter(f.read().split()))

# dict=dict()
# with open('T:\\Programmes\\Python\\Data Science\\52_MCA_DataScience_Lab\\Files\p3\\freequency.txt') as f:
#     data=f.read().split()
#     words={}
#     for i in data:
#         i=i.lower()
#         if i in words:
#             words[i]+=1
#         else:
#             words[i]=1
# for keys in words.keys():
#     print(str(keys)+" : "+str(words[keys]))

