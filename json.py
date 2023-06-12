import json
with open("C://Users//yusuff.sheriff//Downloads//words.json","r",encoding="utf-8")as file :
    data_1=file.read()
data=json.loads(data_1)
print("data",type(data))
#print(data)
dict={}
dict_1={}
for i in data:
    car=i["word"]
   # print(car)
    van=i["meanings"]
    #print(van)
    for j in van:
        dell=j["partOfSpeech"]
       # print(dell)
        man=j["definitions"]
        #print(man)
        list=[]
        for k in man:
            list.append(k["definition"])
            print(list)
            dict[dell]=list
            print(dict)
        dict_1[car]=dict
        print(dict_1)
with open("C://Users//yusuff.sheriff//Downloads//wo.json","w") as file :   
    var=file.write(json.dumps(dict_1, indent=2))   
    print(var)    

