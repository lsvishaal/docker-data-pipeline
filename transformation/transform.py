#transformation/transform.py

import json
def transform_data():
    with open('/data/data.json') as f:
        data = json.load(f)

    #Example Transformation: only keep completed tasks
    completed_tasks = [item for item in data if item['completed']]
    print(f'Transformed Data: {completed_tasks[:5]}')
    return completed_tasks

if __name__ == "__main__":
    transform_data()
    