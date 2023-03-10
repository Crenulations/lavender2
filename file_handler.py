import csv



## =========  PRIMARY LOGS ===========

def write_primary_log_file(log_data):
    with open('data/PrimaryLogs.csv', "a") as outfile:
        writer = csv.DictWriter(outfile, log_data.keys())
        writer.writerow(log_data)

def read_primary_log_file():
    with open('data/PrimaryLogs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            print(', '.join(row))


## =========  BUDGET  ===========

def write_budget_file(data):
    with open('data/PrimaryLogs.csv', 'w', newline='') as csvfile:
        for key in data.keys():
            csvfile.write("%s,%s\n" % (key, data[key]))

def read_budget_file():
    with open('data/PrimaryLogs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            print(', '.join(row))


## =========  Diet  ===========

def write_diet_log_file(diet_data):
    csv_columns = ['date','food_name', 'protein', 'carbs', 'fat', 'calories', 'dairy', 'fruit', 'vegetable']

    with open('data/DietLogs.csv', "a") as outfile:
        writer = csv.DictWriter(outfile, diet_data.keys())
        writer.writerow(diet_data)

def read_diet_log_file():
    with open('data/DietLogs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            print(', '.join(row))