import json

with open('ss.json','r',encoding='utf-8') as f:
    sss = json.load(f)

    for i in range(len(sss)):
        if sss[i]['h_推文總數']:
            pass
            
        else:
            sss[i]['h_推文總數']['all'] = 0
    
    n = sorted(sss,key = lambda x:x['h_推文總數']['all'],reverse=True)
    
    for i in range(len(sss)):
        if n[i]['h_推文總數']['all'] == 0:
            n[i]['h_推文總數']= {}
            
    print(json.dumps(n,indent=4,ensure_ascii=False))