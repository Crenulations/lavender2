import csv



## =========  PRIMARY LOGS ===========

def write_primary_log_file(log_data):
    with open('data/PrimaryLogs.csv') as inf:
        reader = csv.reader(inf.readlines())

    with open('data/PrimaryLogs.csv', 'w') as outf:
        writer = csv.writer(outf)
        previous_log = False
        for line in reader:
            if line[0] == log_data["date"].strftime('%Y-%m-%d'):
                dict_writer = csv.DictWriter(outf, log_data.keys())
                dict_writer.writerow(log_data)
                previous_log = True
                break
            else:
                writer.writerow(line)
        if not previous_log:
            dict_writer = csv.DictWriter(outf, log_data.keys())
            dict_writer.writerow(log_data)
        writer.writerows(reader)
    return True


def get_individual_log(date):
    with open('data/PrimaryLogs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip first line

        data = []
        for row in reader:
            if(row[0] == date.strftime('%Y-%m-%d')):
                data = list(row)
                return data
        return False

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

def get_diet_item_list():
    with open('data/DietLogs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip first line

        data = []
        for row in reader:
            item = list(row)
            data.append(item)
        return data

def read_diet_log_file():
    with open('data/DietLogs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            print(', '.join(row))