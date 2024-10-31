import time
# ----------------------------------------------------------------------
# DATA FROM THE LEADERBOARD
data = "data.csv"
output_file = "result.csv"
import pandas as pd
import requests
df = pd.read_csv(data, index_col=0)

name = df[df.columns[0]].to_list()
email = df[df.columns[1]].to_list()
links = df[df.columns[2]].to_list()

# I AM NOT THE OWNER OF THIS API AND ONLY USING IT FOR THE PROJECT!
api = "https://arcadehelper.tech/api/jam?url="

df2 = pd.DataFrame(columns=["Name", "Email", "Public url", "completionPercentage"])

for i in range(len(links)):
    url = api + links[i]
    
    for j in range(5):
      try:
        response = requests.get(url)
        if response.status_code != 200:
          ConnectionError
        else:
          result : dict = response.json()
          break
      except Exception as err:
        print(f"An error occurred -> {err}")
        time.sleep(2)
        
      
    print(f"Name: {name[i]}, ", end="")
    completionPercentage = float(result["completionPercentage"])
    # completionPercentage = float(points)
    print(f"completionPercentage: {completionPercentage}", end="\n")

    new_data = {"Name": name[i],
                "Email": email[i],
                "Public url": links[i],
                "completionPercentage": completionPercentage,
                }
    # to add data in the dataFrame
    df2.loc[len(df2)] = new_data
    time.sleep(1)
    
# sort the data wrt arcade points
resulted = df2.sort_values(by="completionPercentage", ascending=False)
resulted.to_csv(output_file, index=0)
exit()