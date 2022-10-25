import json


def oplists(k):
    oplist = '''{"096": "Kyivstar","050": "Vodafone","093": "Lifecell"}'''
    oplist = json.loads(oplist)
    return (oplist[k])


with open('data.json', 'r', encoding='utf-8') as f:
    parse = json.load(f)
    k = 0
    while k <= (len(parse["items"])-1):
        print("Name: " + parse["items"][k]["name"])
        print("Num: " + parse["items"][k]["number"][6:])
        print(oplists(parse["items"][k]["number"][3:6]))
        k += 1

f.close()
