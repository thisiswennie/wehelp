import urllib.request as request
import json

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
    data = json.load(response)  # 利用json模組處理json資料格式

# 將景點名稱列表出來
clist = data["result"]["results"]

jpg_urls = {}

with open("attraction.csv", "w", encoding="utf-8") as file:
    for item in clist:
        stitle = item["stitle"].strip()
        address = item["address"]
        longitude = item["longitude"]
        latitude = item["latitude"]
        file_list = item["file"].split(",")
        file_list = [url.strip().lower() for url in file_list] if file_list else None
        first_url = file_list[0].strip() if file_list else None
        jpg_idx = first_url.find(".jpg")
        if jpg_idx != -1: 
            jpg_urls[item["stitle"]] = first_url[:jpg_idx + 4]

        jpg_url = jpg_urls.get(item['stitle'], '')

        file.write(stitle + "," + address[5:8] + "," + longitude + "," + latitude + "," + jpg_url + "\n")
        

classified_data = {}

for item in clist:
    stitle = item["stitle"]
    station = item["MRT"]

    if station in classified_data:
        classified_data[station].append(stitle)
    else:
        classified_data[station] = [stitle]
with open("mrt.csv", "w", encoding="utf-8") as file:
    for station, stitle_list in classified_data.items():
        stitles_str = ", ".join(stitle_list)  # 將景點名稱清單轉為以逗號分隔的字串
        file.write(f"{station}, {stitles_str}"+ "\n")


