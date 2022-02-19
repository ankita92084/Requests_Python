import requests
import json
url=requests.get("https://api.merakilearn.org/courses")
re=url.json()
with open("courses.json","w") as file:
    json.dump(re , file , indent=4)
r = open("courses.json","r")
read = r.read()
data = json.loads(read)
print()
print("Welcome to Navgurukul and learn basic promming language")
print()
i = 0
while i < len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i+=1
progrm_num=int(input("enter the program number:"))
print(data[progrm_num-1]["name"],data[progrm_num-1]["id"])
print()
rp=data[progrm_num-1]["name"]+"_ "+data[progrm_num-1]["id"]+".json" 
link="http://api.merakilearn.org/courses/"+data[progrm_num-1]["id"]+"/exercises"
ur=requests.get(link)
d=ur.json()
with open(rp,"w") as f:
    json.dump(d,f,indent=4)
ret= open(rp,"r")
read = ret.read()
deta = json.loads(read)
i = 0
while i < len(deta["course"]["exercises"]):
    print(str(i+1)+".",deta["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("enter the topic no:- "))
topic  = topic-1
i = 0
while i < len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic <= len(deta["course"]["exercises"]):
    pn= input("previous or next(p&n):")
    if  pn == "p" and pn!= "n":
        topic-=1
        if pn == "p" and topic >1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else :
            i = 0
            while i < len(deta):
                print(str(i+1),deta["course"]["exercises"][i]["name"])
                i+=1
    elif  pn == "n" and pn!="p":
        topic+=1
        if pn== "n" and topic < len(deta["course"]["exercises"]):
                print(deta["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(deta["course"]["exercises"][topic]["content"]):
                    print(deta["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(deta["course"]["exercises"]):
            print("topic is completed.")
            break
    else:
        print("wrong user_input ")
        break   