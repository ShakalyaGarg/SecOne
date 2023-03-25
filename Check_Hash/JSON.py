import requests
import json

def func(placeholder):
    #Defining and obtaining the url for respective hash value
    #placeholder="C090547547F37AE6BB81EFB88D77D3D04C994DCCB94A1E9829A1BAA1CE6782B7"
    url = "https://www.virustotal.com/api/v3/files/" + placeholder

    headers = {
        "accept": "application/json",
        "x-apikey": "4ab826c543206d45073f7f5fea0a5d5ed9eaf23a8b8e49b4190287a741287933"
    }

    response = requests.get(url, headers=headers)
    data=json.loads(response.text)
    dat_list=[]

    #Finding the respective object for which vulnerability analysis is to be done
    for dat in data['data']['attributes']['last_analysis_results']:
        dat_list.append(dat)

    #Storing the vulnerabilities in a text file
    fw=open('sample.txt','w')
    for element in dat_list:
        for dat in data['data']['attributes']['last_analysis_results'][element]['category']:
            fw.write(dat)
        fw.write('\n')
    fw.close()
    fr=open('sample.txt')

    #counting the number of objects and detecting any malicious vulnerabilities
    count=count1=0
    text=fr.readlines()
    fr.close()
    for line in text:
        count+=1
        if not (line=='undetected\n' or line=='type-unsupported\n'):
            count1+=1
    print("Total Scanned : "+ str(count) + "    Detected : " + str(count1))
