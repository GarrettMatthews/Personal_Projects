import pdf_split
import survey_read
import html_read


def main():
    pdf_split.main()
    print("Finished Splitting")
    survey_read.main()
    print("Finished Converting to HTML")
    html_read.main()
    print("Finished Parsing")


if __name__ == '__main__':
    main()
