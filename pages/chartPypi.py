from taipy.gui import Markdown 
from datetime import datetime, timedelta
import os
from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()


client = bigquery.Client(os.getenv("projectGooglCloud"))

packagePypi = "pytest"

def change_input(state):
    state.dataPypi = getLast7daysDownloadPackage(state.packagePypi)

def getLast7daysDownloadPackage(packageName:str)->list:
    print(packageName)

    queryStr = """
        SELECT
          COUNT(*) AS num_downloads,
        DATE_TRUNC(DATE(timestamp), DAY) AS `day`
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE file.project = '{package}'
        AND DATE(timestamp)
        BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY), DAY)
        AND CURRENT_DATE()
        GROUP BY `day`
        ORDER BY `day` DESC
        """.format(package=packageName)



    query_job = client.query(queryStr)



    results = query_job.result()  # Waits for job to complete.
    listDownload = []
    listDays =[]
    for row in results:
        listDownload.append(row.num_downloads)
        listDays.append(row.day)

    if listDownload and len(listDownload) > 0:
                
                
        dataForChart = {
            "downloads":listDownload,
            "day":listDays,
                    
        }
                
                
        return dataForChart
    else:
        return []

dataPypi = getLast7daysDownloadPackage(packagePypi)

pagePypi = Markdown("""
# Stats *Pypi*

Value: <|{packagePypi}|text|>

<|{packagePypi}|input|on_change=change_input|>

<|{dataPypi}|chart|x=day|y=downloads|>
""")