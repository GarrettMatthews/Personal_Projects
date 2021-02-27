import csv

def csv_reader(csv_file):
    """Function to read in a CSV as a nested list, and then clean the \n from each item"""
    data = []
    with open(csv_file, 'r') as csvfile:
        for line in csvfile:
            temp = []
            for i in line.split(','):
                temp.append(i)
            data.append(temp)

    for i in range(len(data)):
        data[i] = [x.replace('\n', '') for x in data[i]]

    return data


def csv_write(csv_file, lyst):
    file = open(csv_file, 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(lyst)
    print("Writing Successful")