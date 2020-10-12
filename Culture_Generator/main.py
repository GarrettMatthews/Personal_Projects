import random
import csv


def country_read():
    """Reads the country CSV in and prepares it"""
    country = open("countries.csv", 'r')
    country = country.readlines()[1:]
    con_lyst = []
    for line in country:
        lyst = []
        for i in line.split(','):
            lyst.append(i)
        con_lyst.append(lyst)

    for i in range(len(con_lyst)):
        con_lyst[i] = [x.replace('\n', '') for x in con_lyst[i]]

    final_lyst = []
    for i in range(len(con_lyst)):
        final_lyst.append(con_lyst[i][0])
    return final_lyst


def random_country(lyst):
    """Returns a random country from a list of countries"""
    numb = random.randint(0, len(lyst))
    return lyst[numb]


def country_record(country):
    """Records the country to a list to limit results to new countries"""
    record = open("record.csv", 'r')
    rec_lyst = []
    for line in record:
        for i in line.split(','):
            rec_lyst.append(i)

    for i in range(len(rec_lyst)):
        rec_lyst[i] = [x.replace('\n', '') for x in rec_lyst[i]]

    if country in rec_lyst:
        present = True
    else:
        present = False

    rec_lyst.append(country)
    final_lyst = []
    for i in rec_lyst:
        temp = [i]
        final_lyst.append(temp)
    file = open("record.csv", 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(final_lyst)
    return present


def main():
    """Main function to run the program"""
    lyst = country_read()
    country = random_country(lyst)
    ans = input("Do you want to at all countries or only at new countries? Please enter 'all' or 'new'>> ")
    if ans in ['all', 'All', 'ALL']:
        country_record(country)
    else:
        present = country_record(country)
        while present:
            country = random_country(lyst)
            present = country_record(country)
    print("And the country of the week is... " + '\n'+'\n' + country + "!")


if __name__ == '__main__':
    main()
