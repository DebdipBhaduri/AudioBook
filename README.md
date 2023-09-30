


# Interactive PDF Text-to-Speech

## Overview

The **Interactive PDF Text-to-Speech** is a Python script that allows users to read the text content of a PDF file interactively. It utilizes the `pyttsx3` library for text-to-speech synthesis and the `PyPDF2` library for PDF manipulation. The script provides a menu-based interface that enables users to choose which page of the PDF they want to read.

## Features

- **Read PDF Pages:** Users can select a specific page number to have the text content of that page read aloud.
- **Interactive Menu:** The script presents an interactive menu that allows users to choose between reading pages and exiting the program.
- **Error Handling:** Input validation ensures that users provide valid page numbers, and it offers feedback for invalid inputs.
- **Text-to-Speech:** The script utilizes the `pyttsx3` library to convert text to speech and provide an auditory reading experience.

## Getting Started

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/DebdipBhaduri/pdf-text-to-speech.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf-text-to-speech
   ```

3. Install the required dependencies (ensure you have Python and pip installed):

   ```bash
   pip install pyttsx3 PyPDF2
   ```

4. Place the PDF file you want to read in the same directory as the script and name it "book.pdf" (you can change the file name in the script).

5. Run the script:

   ```bash
   python pdf_text_to_speech.py
   ```

## Usage

1. Upon running the script, you will be presented with a menu:

   ```
   Menu:
   1. Read a Page
   2. Exit
   ```

2. To read a page from the PDF, select option "1" and enter the page number you want to read (between 1 and the total number of pages in the PDF).

3. The script will read the text content of the selected page aloud.

4. You can continue reading more pages or exit the script by selecting option "2."

## Contributing

Contributions to this project are welcome! If you have ideas for improvements, feature requests, or bug reports, please open an issue or submit a pull request. Refer to the [CONTRIBUTING](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

The Interactive PDF Text-to-Speech script relies on the `pyttsx3` library for text-to-speech synthesis and the `PyPDF2` library for PDF manipulation. Special thanks to the contributors of these libraries for their valuable work.

## Contact

For questions, feedback, or inquiries about this project, please contact debdipbhaduri0@gmail.com.

---

