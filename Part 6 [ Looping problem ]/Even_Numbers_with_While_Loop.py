"""
initially keep count = 1
while count < 50 --> then if count % ==0 --> Then print ==> that Even Number which is under the [Count]
count  +=1
"""
count = 1
print("The Even Number are : ")
while count < 50:
    if count % 2 == 0:
        print(count)
    count += 1