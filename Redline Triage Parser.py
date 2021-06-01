import json

res="Path to mans xml"
processid=""
processname=""

def parser():
    with open(res) as f:
        d = xml2json(f.read())
        d =  json.loads(d)
        d = d.get("itemList").get("eventItem")
        op = []
        for data in d:
            if str(processid) == str(data['details']['detail'][1]['value']) and str(processname) == str(data['details']['detail'][3]['value']) and str(data['details']['detail'][0]['value']) == "start":
                row.append(data)
        if row!= []:
            print(row)
            return row
        else:
            print("Not Found")
            return "NA"


for i in range(0,3):
    op=parser()
    processid=op['details']['detail'][1]['value']
    processname=op['details']['detail'][3]['value']