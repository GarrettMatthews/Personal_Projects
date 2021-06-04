import pdftotree
import os


def main():
    file_lyst = []
    for file in os.listdir("./Split"):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):
            fyle = "./Split/" + filename
            file_lyst.append(fyle)

    for i in file_lyst:
        pdftotree.parse(i, html_path="./HTML/")
        print(i + " Converted to HTML \n")


if __name__ == '__main__':
    main()
