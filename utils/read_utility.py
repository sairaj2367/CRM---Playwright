import csv

def read_test_data(test_data_link, test_case_name):
    with open(test_data_link, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[0] == test_case_name:
                print("Running test : " + test_case_name)
                return row[1:]