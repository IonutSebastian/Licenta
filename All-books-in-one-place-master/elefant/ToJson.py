import json
import copy


from tosql import databaseelefant



def to_json(data: list, link: str) -> bool:

    dict = {'1': []}
    fild ={
        "fld": {
            "fld_name": "fld_name",
            "val": ""
        }
    }
    index = 0
    try:
        for i in range(0, len(data), 2):

            dict['1'].append(copy.deepcopy(fild))
            dict['1'][index]["fld"]["fld_name"] = data[i]
            dict['1'][i//2]["fld"]["val"] = data[i+1]
            index += 1
        with open("../data/elefant.json") as file:
            data = list(json.load(file))
            data.append(dict)

        with open("../data/elefant.json", 'w') as file:
            json.dump(data, file)
        databaseelefant(link, dict)
        return True
    except Exception as e: # work on python 3.x
        print('Failed to upload to ftp: '+ str(e))

        return False

