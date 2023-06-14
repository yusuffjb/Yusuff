import json
with open("C://Users//yusuff.sheriff//Downloads//sample_data (1).json","r")as file :
    data_1=file.read()
data=json.loads(data_1)
#print(data)

list_1=[]
details=data["parametersList"]
#print(details)
for para in details:
    dict = {}
    details1=para['parameterName']
    #print(details1)
    details2=para['max']
    details3=para['min']
    details4=para['avg']
    #print(details1)
    #print(details2)
    #print(details3)
   # print(details4)
    dict['parameterName']=para["parameterName"]
    dict['min_value']=para["min"]
    dict['max_value']=para["max"]
    dict['avg_value']=para['avg']
    #print(dict)
    list_1.append(dict)
print(list_1)
with open("C://Users//yusuff.sheriff//Downloads//t.json","w") as file :
    details=file.write(json.dumps(list_1, indent=2))
    print(details)

