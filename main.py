import os
import requests
from concurrent.futures import ThreadPoolExecutor
import zipfile




folder = "downloads"

def download_file(url):
    try:
        os.makedirs(folder, exist_ok=True)
        filename = url.split("/")[-1]
        filepath = os.path.join(folder, filename)
        response = requests.get(url, stream=True,timeout=20)

        if response.status_code !=200:
            print(f" failed to download:{url} with status code {response.status_code}")
            return
        
    
        with open(filepath,"wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"downloaded: {filename}")
    except Exception as e:
        print(f"failed: {url} as {e}")
        

urls =  [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

 

def unzip_file():
    for file_name in os.listdir(folder):
        full_path = os.path.join(folder, file_name)

        print("Checking:", full_path)

        if file_name.endswith(".zip") and os.path.isfile(full_path):

            
            if not zipfile.is_zipfile(full_path):
                print("Skipping invalid zip file:", file_name)
                continue

            print("Unzipping:", file_name)

            with zipfile.ZipFile(full_path, 'r') as zip_ref:
                zip_ref.extractall(folder)

            print("Deleting:", full_path)
            os.remove(full_path)   

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(download_file, urls) 


unzip_file()            
