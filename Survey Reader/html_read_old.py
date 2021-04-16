import nltk
from bs4 import BeautifulSoup
import os
import csv
# nltk.download('punkt')


def main():
    print("Starting to parse")
    file_lyst = []

    for file in os.listdir("./HTML"):
        filename = os.fsdecode(file)
        if filename.endswith(".html"):
            fyle = "./HTML/" + filename
            file_lyst.append(fyle)
    for i in file_lyst:
        print(i)
        survey_list = [["Date", "Time", "Pit", "Product", "Yards", "Conv_Factor", "Tons", "Notes"]]
        with open(i, 'rb') as html:
            soup = BeautifulSoup(html, 'html.parser')
            clean = soup.get_text()
            tokens = nltk.word_tokenize(clean)
            if "-" in tokens:
                pit = str(' '.join(tokens[0:tokens.index("-")]))
            else:
                pit = i + "Pit issue"
            if "Cubic" in tokens:
                date = str(tokens[tokens.index("Cubic") - 3])
            else:
                date = i + "Date missing"
            if "Cubic" in tokens:
                time = str(' '.join(tokens[tokens.index("Cubic") - 2: tokens.index("Cubic")]))
            else:
                time = i + "Time missing"
            if "-" in tokens and ":" in tokens:
                product = str(' '.join(tokens[(tokens.index("-") + 1):(tokens.index("Cubic")-3)]))
            else:
                product = i + "Product missing"
            if "Yards" in tokens:
                yards = str(tokens[tokens.index("Yards")+2])
            else:
                yards = i + "Yards missing"
            if "Conversion" in tokens:
                conv_factor = str(tokens[tokens.index("Conversion")+2])
            else:
                conv_factor = i + "conversion factor missing"
            if "Collected" in tokens:
                tons = str(tokens[tokens.index("Collected")-1])
            else:
                tons = i + "Tons missing"
            if "Notes" in tokens and "Cubic" in tokens:
                note = str(' '.join(tokens[tokens.index("Notes")+1:tokens.index("Cubic")]))
            else:
                note = ""
            temp = (date, time, pit, product, yards, conv_factor, tons, note)
            survey_list.append(temp)
        save_file = "./survey_save.csv"
        if os.path.isfile(save_file):
            survey_list = survey_list[1:]
        file = open(save_file, 'a', newline='', encoding="UTF-8")
        with file:
            write = csv.writer(file)
            write.writerows(survey_list)
            print("File written")
        print(i, " successfully parsed \n")


if __name__ == '__main__':
    main()
