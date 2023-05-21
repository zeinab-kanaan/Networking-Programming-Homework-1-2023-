import json
from pprint import pprint
print ("x=4","y=5","z=6")
s=0
q1 = {}
L1 = []
name1 = input("enter name :")
with open("q.json","r") as f:
    q=json.loads(f.read())
    for i in q :
        print(i)
        ans = input("enter the answer a/b :")
        L1.append(ans)
        if ans ==q[i]:
            print("correct answer,you got 1 point")
            s=s+1
        else:
            print("wrong answer,you lost 1 point")
            s=s-1

    q1 ={name1:L1}
    print(q1)

    print("final score is :",s)
q2=json.dumps(q1)
with open("q1.json","w")as f:
    f.write(q2)
