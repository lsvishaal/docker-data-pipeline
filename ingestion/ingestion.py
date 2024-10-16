import requests
import os
import json

def fetch_data():
    # Fetch data from the API
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    print(f"Data Fetched: {data[:5]}")  # Prints first 5 items

    # Save data to /data/data.json
    output_dir = "/data"
    
    # Check if the directory exists, create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Specify the output file path
    output_file = os.path.join(output_dir, "data.json")

    # Write data to file in JSON format
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Data saved to {output_file}")
    return data

if __name__ == "__main__":
    fetch_data()
