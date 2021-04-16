from array import array
import numpy as np
predictions = ['POSITIVE', 'NEUTRAL', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'POSITIVE', 'NEUTRAL', 'NEUTRAL', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL', 'POSITIVE', 'NEUTRAL', 'POSITIVE', 'POSITIVE', 'POSITIVE', 'NEUTRAL', 'NEUTRAL', 'NEUTRAL', 'POSITIVE']
months = ['April', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'March', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'February', 'January', 'January', 'January', 'January', 'January', 'January', 'January']
new_lst = []
unique_months = []
Positive = []
Neutral = []
Negative = []
for i in months:
    if i not in unique_months:
        unique_months.append(i)

for x in range(len(unique_months)):
    for i in range(len(months)):
        if months[i] == unique_months[x]:
            new_lst.append(predictions[i])
    Positive.append(new_lst.count("POSITIVE"))
    Neutral.append(new_lst.count("NEUTRAL"))
    Negative.append(new_lst.count("NEGATIVE"))
    new_lst = []

# print(Positive)
# print(Neutral)
# print(Negative)
Positive_linechart = np.array(Positive)
Positive=Positive[::-1]
# print(Positive)

# print(predictions.count("POSITIVE"))
# print(predictions.count("NEUTRAL"))
# print(predictions.count("NEGATIVE"))


pos = [5,3,0,1,0]
neu = [6,9,4,8,1]
neg = [3,4,3,3,0]

if len(pos)<6:
    while(len(pos)!=6):
        pos.insert(0,0)

print(pos)