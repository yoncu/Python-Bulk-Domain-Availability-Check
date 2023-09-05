import requests;
import json;

headers = {
	"Accept": "application/json",
	"Referer": "https://www.yoncu.com",
	"User-Agent": "Python-YoncuAPI"
};
curl = requests.post('https://www.yoncu.com/YoncuTest/YoncuSec_Token', headers=headers);
headers["Cookie"]="YoncuSec-v1="+curl.text;
curl = requests.post('https://www.yoncu.com/API/Domain/Check', data=json.dumps({"domain":["asd123web.com","yoncu.net","domain.org","turkey.biz","turkce.com.tr","sitem.tr","dollar.day","olmayantld.k1o"]}), headers=headers);
array = json.loads(curl.content);
if array[0]:
    for Domain, Info in array[1].items():
        print(Domain+" - "+Info["message"]+" - "+Info["register"]["message"]+" "+Info["register"]["details"]);
else:
    print("API ERROR: "+str(array[1]));
