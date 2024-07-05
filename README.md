# PDF-Security
This project provides a simple and effective solution for encrypting PDF files using PyPDF2. The script allows users to set a password for their PDF documents, ensuring that only authorized individuals can access the content.

![](https://s.smallpdf.com/static/cms/f/102628/300x180/3865649eef/8bfe6e572c81ad5bdc63.svg)
## Problem Statement:
In today's digital world, sensitive information is often shared through PDF files. However, without proper encryption, these files are vulnerable to unauthorized access and data breaches. Ensuring the confidentiality and security of PDF documents is crucial for protecting sensitive information.

## Objective:
The objective of this project is to provide a simple and effective solution for encrypting PDF files. By implementing password protection, we can ensure that only authorized individuals have access to the content of the PDF documents.

## Solution:
This script allows you to encrypt a PDF file with a password using PyPDF2. It prompts the user for a password and a new file name, then encrypts the PDF and saves it with the specified name.

## Requirements:

* Python 3.x
* PyPDF2 library
## Installation:

* Clone the repository or download the script.
```bash
git clone https://github.com/Banner-19/PDF-Security.git
```
* Ensure you have Python 3 installed on your system.
* Install the PyPDF2 library if you haven't already:
```bash
pip install PyPDF2
```
## Usage:

* Place the PDF file you want to encrypt in the same directory as the script.
* Run the script:
```bash
python protector.py
```
* Follow the prompts to enter a password and specify a new name for the encrypted PDF file.
__Note:__ You can use `regression_analysis.pdf` for encryption.
### Example:
```bash
Enter your password: my_secure_password
Password was set successfully!
What will you name your encrypted pdf? (without ".pdf"): encrypted_file
Excellent! You have secured your PDF file!
```
