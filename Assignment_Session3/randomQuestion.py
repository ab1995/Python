import random

questList = ["Quest_1", "Quest_2", "Quest_3", "Quest_4", "Quest_5", "Quest_6", "Quest_7", "Quest_8"]

count=5
while count>0:
    print(random.choice(questList))
    count-=1