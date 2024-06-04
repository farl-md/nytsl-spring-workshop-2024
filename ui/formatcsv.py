import csv
import os

def main():

    data = []

    with open(os.path.join(os.getcwd(), "data/step_1.csv"), "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [r for r in reader]

    sort = {}

    for i, row in enumerate(data):
        sort[str(i + 1)] = 'http://127.0.0.1:8000/' + row['ark']

    for row in data:
        if row['relation'] in sort:
            row['relation'] = sort[row['relation']]

    for row in data:
        if row['source'] in sort:
            row['source'] = sort[row['source']]

    with open(os.path.join(os.getcwd(), "data/for_update.csv"), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    return data

if __name__ == "__main__":
    main()