from taipy.gui import Markdown
from datetime import datetime, timedelta
from  helpers import npmApiHelper

# page state
packageNpm = ""
versionsNpm = {
     "version":[],
     "npm":[],
     "node":[]
}
dataDownloadNpm = {
    "day":[],
    "downloads":[]
}
datesNPM = [(datetime.now() - timedelta(days=7)).date(), datetime.now().date()]

def change_input(state):
    if state.packageNpm and len(state.packageNpm) > 0:
        infoPackage =npmApiHelper.getPackageInfos(state.packageNpm)
        state.versionsNpm = formatNpmVersionTable(infoPackage.get("versions",{}))
        state.dataDownloadNpm = npmApiHelper.getTimedDownloadPackage(state.packageNpm, state.datesNPM[0], state.datesNPM[1])

    
def formatNpmVersionTable(dataVersions:dict):
    try:
        print(len(dataVersions))
        if dataVersions and len(dataVersions) > 0:
            #versionsKeys:list =sorted(dataVersions.keys(),reverse=True)
            #print(versionsKeys)
            versionsNpm = {
                "version":[dataVersions[v].get("version") for v in dataVersions.keys()],
                "npm":[dataVersions[v].get("_npmVersion","") for v in dataVersions.keys()],
                "node":[dataVersions[v].get("_nodeVersion","") for v in dataVersions.keys()]
            }

        
            return versionsNpm
        return {"version":[],"npm":[],"node":[]}
    except Exception as e:
        print(e)
        return {"version":[],"npm":[],"node":[]}

layoutNpm = {
  "xaxis": {
    "title": "Period"
  },
  "yaxis": {
    "title": "Nb of downloads"
  },
}


pageNpm_md = Markdown("chartNpm.md")
