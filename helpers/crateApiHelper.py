import requests

def getVersionsPackage(packageName):
    output = {"version":[],"rust":[]}
    response =requests.get("https://crates.io/api/v1/crates/"+ packageName)
    if response and response.status_code == 200:
        dataRaw = response.json()
        output["version"] = [v.get("num") for v in dataRaw.get("versions")]
        output["rust"] = [v.get("rust_version") for v in dataRaw.get("versions")]
    return output
    
def getLastDownload(packageName:str):
    output = {"day":[],"downloads":[]}
    response =requests.get("https://crates.io/api/v1/crates/"+ packageName +"/downloads")
    if response and response.status_code == 200:
        dataRaw = response.json()
        structureDownloadGlobal = {}
        if dataRaw.get("version_downloads") and len(dataRaw.get("version_downloads")) > 0:
            
            for stat in dataRaw.get("version_downloads"):
                if stat.get("date") not in structureDownloadGlobal.keys():
                    structureDownloadGlobal[stat.get("date")] = stat.get("downloads")
                else:
                    structureDownloadGlobal[stat.get("date")] += stat.get("downloads")
                

        if dataRaw.get("meta") and dataRaw.get("meta",{}).get("extra_downloads") and len(dataRaw.get("meta",{}).get("extra_downloads")) > 0:
            for stat in dataRaw.get("meta",{}).get("extra_downloads"):
                if stat.get("date") not in structureDownloadGlobal.keys():
                    structureDownloadGlobal[stat.get("date")] = stat.get("downloads")
                else:
                    structureDownloadGlobal[stat.get("date")] += stat.get("downloads")

        if structureDownloadGlobal:
            listPossibleDate = sorted(set([key for key in structureDownloadGlobal]))

            for day in listPossibleDate:
                output["day"].append(day)
                output["downloads"].append(structureDownloadGlobal[day])


    return output