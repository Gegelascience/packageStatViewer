import os
from google.cloud import bigquery
from dotenv import load_dotenv
load_dotenv()

client = bigquery.Client(os.getenv("projectGooglCloud"))

def getLast7daysDownloadPackage(packageName:str)->list:
    print(packageName)

    try:
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
        print("exception")
        return {"day":[],"downloads":[]}