import requests
import json
#1
url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url)

if response.status_code == 200:
   
    with open("robots_wikipedia.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("File saved successfully.")
else:
    print(f"Error on upload: {response.status_code}")
#############################################
    
#2
urls = [
    "https://russianwarship.rip/api/v2/war-info",
    "https://russianwarship.rip/api/v2/war-info/status"
]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
    
        data = response.json()

     
        file_name = url.split("/")[-1] + ".json"

       
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Data from {url} saved to file {file_name} successfully.")
    else:
        print(f"Error loading from {url}: {response.status_code}")