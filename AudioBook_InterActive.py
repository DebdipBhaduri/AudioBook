import pyttsx3
import PyPDF2

def read_page(pdf_reader, page_number):
    if 1 <= page_number <= len(pdf_reader.pages):
        page = pdf_reader.pages[page_number - 1]
        return page.extract_text()
    else:
        return "Invalid page number. Please enter a valid page number."

# Initialize the text-to-speech engine
Debdip = pyttsx3.init()

# Open the PDF file using a context manager
with open("book.pdf", mode="rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    print(f"Total number of pages in the PDF: {num_pages}")

    while True:
        print("\nMenu:")
        print("1. Read a Page")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            page_number = int(input(f"Enter the page number to read (1-{num_pages}): "))
            text = read_page(pdf_reader, page_number)
            Debdip.say(text)
            Debdip.runAndWait()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

print("Goodbye!")
