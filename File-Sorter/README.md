# File-Sorter

## Description
**File-Sorter** is a program that organizes and refactors your files from a single input folder into multiple output folders based on their file extensions.

## Usage Instructions
To configure and use the program, follow these steps:

1. Open the `pathdict.py` file. This file contains a key-value dictionary where:
   - **Keys**: File extensions (`.mp4`, `.txt`, `.jpg`).
   - **Values**: Names of the folders where files with the corresponding extensions will be moved.
2. Modify the **values** in the dictionary to match the folder names you want to use.
3. **Do not change or add new keys**, unless you also modify the program to handle the new keys. Changing keys without updating the code can lead to crashes.
4. Ensure that the input and output folders, as well as the program itself, are located on the **same disk**.

## Notifications
- Ensure that the files to be sorted have **only one `.`** in their names before the file extension.
  - Example: `document.txt` is valid, but `my.document.txt` may cause issues.
- After starting the program, allow **10–15 seconds** for it to complete the sorting. Python is a relatively slow language for certain tasks.

---

Enjoy effortless file organization with **File-Sorter**!
