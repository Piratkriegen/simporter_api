from fastapi import FastAPI
from datetime import datetime

import pandas as pd
import time
import sqlite3

app = FastAPI()

@app.get("/")
def root():
    return {"greeting" : "hello"}

@app.get("/api/info")
def info():
    pass

@app.get("/api/{timeline}")
async def read_timeline(timeline):
    # start_date = int(
    #     time.mktime(datetime.strptime(startDate, "%Y-%m-%d").timetuple()))
    # end_date = int(
    #     time.mktime(datetime.strptime(startDate, "%Y-%m-%d").timetuple()))

    # data = select_db(startDate, endDate)
    # data = filter_data(data)

    return {'timeline': timeline}

# {
#         "timeline": [{
#             "startDate": start_date,
#             "endDate": end_date,
#             "Type": Type,
#             "Grouping": Grouping,
#             "attr1": attr1,
#             "attr2": attr2
#         }]
#     }


# startDate, endDate, Type, Grouping, attr1, attr2

def filter_data(df, **att):

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)

    return df

PATH_TO_DATA = "simporter_api/data/data.db"

def select_db(startDate, endDate):
    conn = sqlite3.connect(PATH_TO_DATA)
    c = conn.cursor()

    query = f"""
        SELECT *
        FROM data
        WHERE timestamp BETWEEN ? AND ?
        """
    c.execute(query, (startDate, endDate))
    db = c.fetchall()
    df = pd.DataFrame(
                        db,
                        columns=[
                            'asin', 'brand', 'id', 'source',
                            'stars', 'timestamp'
                            ],
                    )
    return df
