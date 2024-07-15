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
api = "https://arcadehelper.vercel.app/api/search?url="

df2 = pd.DataFrame(columns=["Name", "Email", "Public url", "Points", "Eligibility", "Swags"])

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
    points = result["totalPoints"]
    points = float(points)
    print(f"Total Points: {points}", end="\n")

    # for the eligibility
    if points >= 10:
      eligible = True
    else:
      eligible = False
      arcadeSwags = "NULL"

    if eligible and points < 25:
      arcadeSwags = "Standard Milestone"

    elif eligible and points < 40:
      arcadeSwags = "Advanced Milestone"

    elif eligible and points < 60:
      arcadeSwags = "Premium Milestone"

    elif eligible and points < 70:
      arcadeSwags = "Premium Plus Milestone"

    elif eligible and points >= 70:
      arcadeSwags = "Champions Milestone"

    new_data = {"Name": name[i],
                "Email": email[i],
                "Public url": links[i],
                "Points": points,
                "Eligibility" : eligible,
                "Swags" : arcadeSwags
                }
    # to add data in the dataFrame
    df2.loc[len(df2)] = new_data
    time.sleep(1)
    
# sort the data wrt arcade points
resulted = df2.sort_values(by="Points", ascending=False)
resulted.to_csv(output_file, index=0)
exit()