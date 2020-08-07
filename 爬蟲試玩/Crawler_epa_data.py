# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 15:00:00 2020

@author: MaxLin
"""
import pandas as pd
import calendar
from urllib import request
import json


# Configure 需自行輸入
# https://data.epa.gov.tw/dataset 註冊可拿到LICENSE KEY
API_KEY = "XXXXXXXXX"
# 自行新增各測站對應的ID
SITE_ID = {
    "觀音": 19,
    "湖口": 22,
    "中壢": 68,
    "小港": 58
}


# ===================================================
# 抓環保署空氣品質歷史資料
# 空氣品質監測日平均值(一般污染物)
# https://data.epa.gov.tw/dataset/aqx_p_19/resource/02bfad76-4f15-4d1f-88f9-750b7bf3bb14
# ===================================================
def crawler_air_data_(year, month, site):
    print(f"{year}-{month} {site} air_data loading")
    date_list = []
    for d in range(1, calendar.monthrange(year, month)[1]+1):
        if d < 10:
            date_list.append(f"{year}-{month}-0{d}")
        else:
            date_list.append(f"{year}-{month}-{d}")

    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    columns = ['CH4', 'SO2', 'CO', 'O3', 'NMHC', 'NO', 'PM2.5', 'PM10', 'PH_RAIN', 'AMB_TEMP', 'NO2', 'THC',
               'NOx', 'RH', 'RAIN_INT', 'RAIN_COND', 'WS_HR', 'WIND_SPEED']
    df = pd.DataFrame(columns=["Date"] + columns)
    df["Date"] = date_list

    filters = f"filters=SiteId,EQ,{SITE_ID[site]}"
    url = f"https://data.epa.gov.tw/api/v1/aqx_p_19?format=json&limit=10000&year_month={year}_{month}&api_key={API_KEY}&{filters}"
    res = request.urlopen(url)
    js = json.load(res)
    for j in js["records"]:
        ind = int(j["MonitorDate"][8:]) - 1
        df.loc[ind, j['ItemEngName']] = j['Concentration']
    for c in columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


if __name__ == "__main__":
    pd.set_option('display.width', 500)  # 設定顯示寬度為500，防止輸出內容被換行
    pd.set_option('display.max_columns', None)  # 設定pandas顯示欄位(行)資訊無限制
    pd.set_option('display.max_rows', None)  # 設定pandas顯示欄位(列)資訊無限制

    # 抓環保署歷史數據
    df_air = pd.DataFrame()
    for m in range(1, 13):
        df_temp = crawler_air_data_(2019, m, "小港")
        if m == 1:
            df_air = df_temp.copy()
        else:
            df_air = df_air.append(df_temp, ignore_index=True)
    print(df_air)
    # df_air.to_csv(os.path.join(r"D:\RawData\Weather", "Air_Historic_data.csv"), encoding="utf-8-sig", index=False)
