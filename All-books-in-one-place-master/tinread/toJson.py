import copy
from tosql import databasetinread
def to_json(data:list,idfile:str) ->bool:
    id="1"
    dict = {id: []}
    fild ={
        "fld": {
            "fld_name": "",
            "ind_1": "",
            "ind_2": "",
            "val": "",
            "subflds": []
        },
    }
    subfild={
                "subfld": {
                    "name":"",
                    "val": ""
                },

            }
    index =0
    for i in range(0,len(data)-2,2):
        dict[id].append(copy.deepcopy(fild))
        dict[id][index]["fld"]["fld_name"]=data[i]
        has_sub=data[i+1].find("$")
        value =data[i+1]
        if(has_sub==-1):
            dict[id][i//2]["fld"]["val"]=data[i+1]
        else:
            if(value[0]=="#" or (value[0] >="0"and value[0]<="9")):
                dict[id][index]["fld"]["ind_1"]=value[0]
                value =value[1:]
                if(value[0]==" " and (value[1]=="#" or (value[1] >="0"and value[1]<="9"))):
                    dict[id][index]["fld"]["ind_2"]=value[1]
                    value=value[2:]
            value = value.split("$")
            subfildIndex=0
            dict[id][i//2]["fld"]["val"]=value[0]
            for i in range(1,len(value)):
                if len(value[i])>0:
                    dict[id][index]["fld"]["subflds"].append(copy.deepcopy(subfild))
                    dict[id][index]["fld"]["subflds"][subfildIndex]["subfld"]["name"] = value[i][0]
                    dict[id][index]["fld"]["subflds"][subfildIndex]["subfld"]["val"] = value[i][1:]
                    subfildIndex +=1
        index +=1
    databasetinread(int(idfile),dict)
    return True



