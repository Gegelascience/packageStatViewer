from taipy.gui import Markdown
import requests
from datetime import datetime, timedelta,date

# page state
packageNpm = ""
dataNpm = {
    "day":[],
    "downloads":[]
}
datesNPM = [(datetime.now() - timedelta(days=7)).date(), datetime.now().date()]

def change_input(state):
    if state.packageNpm and len(state.packageNpm) > 0:
        state.dataNpm = getTimedDownloadPackage(state.packageNpm, state.datesNPM[0], state.datesNPM[1])


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



pageNpm = Markdown("""
# Stats *NPM*

<|{packageNpm}|input|label=NPM Package|>
<|{datesNPM}|date_range|label_start=Start Date|label_end=End Date|>
<|Show Stats|button|on_action=change_input|>

<|{dataNpm}|chart|x=day|y=downloads|>
<|{dataNpm}|table|>
""")