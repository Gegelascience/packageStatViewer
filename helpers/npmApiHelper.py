import requests
from datetime import datetime,date

def getTimedDownloadPackage(packageName:str,startDate:date, endDate:date)->list:
    endTime = datetime.combine(endDate, datetime.min.time())
    startTime = datetime.combine(startDate, datetime.min.time())

    responseApi = requests.get("https://api.npmjs.org/downloads/range/" + startTime.strftime("%Y-%m-%d") + ":" + endTime.strftime("%Y-%m-%d") + "/" + packageName)
    if responseApi.status_code == 200:
        try:
            possibleData = responseApi.json()
            if possibleData and len(possibleData) > 0:
                
                
                dataForChart = {
                    "day":[d.get("day") for d in possibleData.get("downloads",[])],
                    "downloads":[d.get("downloads") for d in possibleData.get("downloads",[])]
                }
                
                return dataForChart
            else:
                return {"day":[],"downloads":[]}

        except Exception as e:
            print(e)
            return {"day":[],"downloads":[]}
    else:
        return {"day":[],"downloads":[]}
    

def getPackageInfos(packageName:str):
    responseApi = requests.get("https://registry.npmjs.org/" + packageName)
    if responseApi.status_code == 200:
        possibleData = responseApi.json()
        if possibleData and len(possibleData) > 0: 
            return possibleData
        else:
            return None