import json
import copy

def to_json(data:list,id:str,idcatalog:int) ->bool:
    dict = {id: []}
    fild ={
        "fld": {
            "fld_name": "fld_name",
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
    try:
        for i in range(0,len(data),2):

            dict[id].append(copy.deepcopy(fild))
            dict[id][index]["fld"]["fld_name"]=data[i]
            if(data[i+1].find("|")==-1):
                dict[id][i//2]["fld"]["val"]=data[i+1]
            else:
                value =data[i+1]
                if value[0]!="|":
                    dict[id][index]["fld"]["ind_1"]=value[0]
                    if value[1]!="|":
                        dict[id][index]["fld"]["ind_2"]=value[1]
                value = value.split("|")
                subfildIndex=0
                for i in value:
                    if len(i)>0:
                        dict[id][index]["fld"]["subflds"].append(copy.deepcopy(subfild))
                        dict[id][index]["fld"]["subflds"][subfildIndex]["subfld"]["name"] = i[0]
                        dict[id][index]["fld"]["subflds"][subfildIndex]["subfld"]["val"] = i[1:]
                        subfildIndex +=1
            index +=1
        #databasetinread(idcatalog,dict)
        print (dict)




        return True
    except:
        return False

