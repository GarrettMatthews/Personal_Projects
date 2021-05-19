import csv


def csv_reader(csv_file):
    """Function to read in a CSV as a nested list, and then clean the \n from each item"""
    data = []
    with open(csv_file, 'r') as csvfile:
        line = csv.reader(csvfile)
        for i in line:
            data.append(i)

    return data


def csv_header(lyst):
    """Creates a dictionary of CSV headers with the list index for easier index accessing. INPUT FULL LIST"""
    lyst = lyst[0]
    head_dict = {}
    for i in range(len(lyst)):
        head_dict[lyst[i]] = i
    return head_dict


def csv_write(csv_file, lyst):
    file = open(csv_file, 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(lyst)
    print("Writing Successful")
