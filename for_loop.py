import os
import requests

urls = ("https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip")

# select download directory
folder_name = "downloads"

#create download path, if it does not exist 
os.makedirs(folder_name,exist_ok=True)

#  put in loop so download can occur one url affter another
for url in urls:
    file_name= url.split("/")[-1]
    #create file path
    file_path = os.path.join(folder_name,file_name)
    response = requests.get(url,stream=True)
    # proceed with download
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
            print("Download complete:", file_path)
    else:
        print("Download failed")
print("download complete")        





