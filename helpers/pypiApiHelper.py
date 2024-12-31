import os
from datetime import date
from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()

client = bigquery.Client(os.getenv("projectGooglCloud"))


def getPackagesVersionsList(packageName:str):
    try:
        queryStr = """
        SELECT * FROM `bigquery-public-data.pypi.file_downloads` WHERE file.project = '{packageName}'
        """.format(packageName=packageName)
        query_job = client.query(queryStr)
        results = query_job.result()
        listVersions = []
        listPythonVersion = []
        for row in results:
            listVersions.append(row["file.version"])
            listPythonVersion.append(row["details.python"])
        return {"version":listVersions,"python":listPythonVersion}
    except Exception as e:
        print(e)
        return {"version":[],"python":[]}

def getTimedDownloadPackage(packageName:str, dateStart:date,dateEnd:date)->dict:
    print(packageName)    

    try:

        queryStr = """
            SELECT
            COUNT(*) AS num_downloads,
            DATE_TRUNC(DATE(timestamp), DAY) AS `day`
            FROM `bigquery-public-data.pypi.file_downloads`
            WHERE file.project = '{package}'
            AND DATE(timestamp) BETWEEN  DATE({yearStart},{monthStart},{dayStart}) and DATE({yearEnd},{monthEnd},{dayEnd})
            GROUP BY `day`
            ORDER BY `day` DESC
            """.format(
                package=packageName,
                yearStart=dateStart.year,
                monthStart=dateStart.month,
                dayStart=dateStart.day,
                yearEnd=dateEnd.year,
                monthEnd=dateEnd.month,
                dayEnd=dateEnd.day
                )



        query_job = client.query(queryStr)



        results = query_job.result()  # Waits for job to complete.
        listDownload = []
        listDays =[]
        for row in results:
            print(row)
            listDownload.append(row.num_downloads)
            listDays.append(row.day)

        if listDownload and len(listDownload) > 0:
                    
                    
            dataForChart = {
                "downloads":listDownload,
                "day":listDays,
                        
            }
                    
                    
            return dataForChart
        else:
            print("ko")
            return {"day":[],"downloads":[]}
    except Exception as e:
        print("exception",e)
        return {"day":[],"downloads":[]}