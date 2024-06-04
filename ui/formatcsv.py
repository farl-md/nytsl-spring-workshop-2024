import csv
import os

def main():

    data = []

    with open(os.path.join(os.getcwd(), "data/mint.csv"), "r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [r for r in reader]

    for row in data:
        if row['url'] == 'http://127.0.0.1:8000/':
            row['url'] = row['url'] + row['ark'] + '?json'

    sort = {}

    for i, row in enumerate(data):
        sort[str(i + 1)] = 'http://127.0.0.1:8000/' + row['ark']

    update(data, sort, 'relation')
    update(data, sort, 'source')


    with open(os.path.join(os.getcwd(), "data/model.csv"), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    return data

def update(data, sort, key):

    for row in data:
        if row[key].split('/')[0] in sort:
            if len(row[key].split('/')) > 1:
                num = row[key][:2]
                ext = '/'.join(row[key].split('/')[1:])
                row[key] = sort[num] + '/' + ext
            else:
                row[key] = sort[row[key]]
    return data



if __name__ == "__main__":
    main()