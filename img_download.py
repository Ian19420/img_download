import bs4, requests, os

url = "https://memes.tw/maker"
htmlfile = requests.get(url)
print("網頁下載中...")
htmlfile.raise_for_status()
print("網頁下載成功")

folder = "images"
if os.path.exists(folder) == False:
    os.mkdir(folder)

soup = bs4.BeautifulSoup(htmlfile.text, "lxml")
imgtag = soup.select("img")
print("搜尋到的圖片數量 = ", len(imgtag))

if len(imgtag) > 0:
    for i in range(len(imgtag)):
        imgurl = imgtag[i].get("src") #絕對路徑
        print(f"{imgurl} 圖片下載中...")
        picture = requests.get(imgurl)
        picture.raise_for_status()
        print(f"{imgurl} 圖片下載成功")

        with open(os.path.join(folder, os.path.basename(imgurl)), "wb") as f:
            for save in picture.iter_content(10240):
                f.write(save)