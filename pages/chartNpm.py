from taipy.gui import Markdown 
import requests
from datetime import datetime, timedelta

package = "ngx-view360"

def change_input(state):
    state.data = getLast7daysDownloadPackage(state.package)

def getLast7daysDownloadPackage(packageName:str)->list:
    now = datetime.now()
    SevenDaysAgo =now - timedelta(days=7)
    responseApi = requests.get("https://api.npmjs.org/downloads/range/" + SevenDaysAgo.strftime("%Y-%m-%d") + ":" + now.strftime("%Y-%m-%d") + "/" + packageName)
    if responseApi.status_code == 200:
        try:
            possibleData = responseApi.json()
            if possibleData and len(possibleData) > 0:
                
                
                dataForChart = {
                    "day":[d.get("day") for d in possibleData.get("downloads",[])],
                    "downloads":[d.get("downloads") for d in possibleData.get("downloads",[])]
                }
                
                
                #print(dataForChart)
                
                return dataForChart
            else:
                return []

        except Exception as e:
            print(e)
            return []
    else:
        return []

data = getLast7daysDownloadPackage(package)

pageNpm = Markdown("""
# Stats *NPM*

Value: <|{package}|text|>

<|{package}|input|on_change=change_input|>

<|{data}|chart|x=day|y=downloads|>
""")