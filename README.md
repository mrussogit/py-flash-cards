# Py Flash Cards - Create Flashcards with ReportLab

This Python script generates a PDF of flashcards from a list of sentences stored in a text file. It utilizes the **ReportLab** library to generate the cards in a grid format on A4 paper, each card containing a sentence with customizable formatting. Sentences can include basic formatting such as bold and italics using simple BBCode-like tags.

## Features

- Automatically lays out sentences into 2 columns and 6 rows per page.
- Supports **bold** and *italic* text using `[b]` and `[i]` BBCode tags.
- Customizable card sizes and margins.
- Creates a PDF output with all cards evenly distributed across pages.

## Requirements

You need  `reportlab` for generating PDFs

```bash
pip install reportlab
```

## Usage

### Input

The input to the script is a plain text file (`sentence_list.txt`) where each line represents a sentence that will be placed on a separate card. Example from sentence_list:

```txt
[b]Show, don't tell[/b]: Let readers experience the story through actions, dialogue, and senses rather than exposition.
[b]Create compelling characters[/b]: Characters should have clear goals, motivations, and obstacles that drive the story forward.
```

### Output

The script generates a PDF file (`output_cards.pdf`) with flashcards arranged in a 2x6 grid on each page. Each card will display one sentence from the input file.

![pyflashcard](https://github.com/user-attachments/assets/a9bae064-2418-42f1-b993-27bbcb349a7b)


### Running the Script

To generate the flashcards, place the python script in same directory as sentence_list.txt and run from there from powershell/cmd.

```bash
python pyflashcards.py
```

### Customizing the Input and Output Files

If you want to use different input or output file names, modify the call to `create_cards` at the bottom of the script:

```python
create_cards('your_input_file.txt', 'your_output_file.pdf')
```
Enjoy!
---
