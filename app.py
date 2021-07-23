import requests
import json 
import datetime
import time
from plyer import notification

def grabData(countryname):
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country": countryname}
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    js = json.loads(response.text)
    #print(js)
    result = js.get('response')[0]
    #print(result.get('cases'))
    return result.get('cases'), result.get('deaths'), result.get('tests')

totalCases,totalDeaths,totalTests=grabData("Malaysia")
#print(totalCases)
#print(totalDeaths)
#print(totalTests)

while(True):
        notification.notify(
            app_name ="Covid-19 Notification App",
            title = "COVID19 Stats for {}".format(datetime.date.today()),
            message = "New Cases: "+str(totalCases.get('new')) +"\nNew Deaths: "+str(totalDeaths.get('new')) +"\nTotal Deaths: "+str(totalCases.get('total')) ,
            app_icon = "coronavirus.ico",
            timeout=30
        )
        time.sleep(60*60*24)


    
