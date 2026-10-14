# Random Password Generator — Oasis Infobyte Internship

## Project Overview

A simple Python-based password generator developed as part of my Oasis Infobyte Python Programming Internship. It allows users to generate random passwords by selecting their preferred character types and password length.

## Features

- Generates random passwords based on the length specified by the user.
- Supports lowercase letters, uppercase letters, numbers, and symbols.
- Enforces a minimum password length of 8 characters.
- Validates character-type selections and requires at least two character types.
- Validates yes/no responses.
- Allows users to generate multiple passwords without restarting the program.

## Technologies Used

- **Python** — Main programming language.
- **random** — Generates random selections.
- **string** — Provides collections of letters, digits, and punctuation characters.

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python password_generator.py
```

4. Enter the desired password length.
5. Select the character types to include.
6. Choose whether to generate another password.

## Project Structure

```text
random-password-generator/
├── password_generator.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Limitations

- The program runs in a terminal rather than a graphical interface.
- Users must select at least two character types.
- The generated password's security depends on the implementation and selected character options.

## Future Improvements

- Use Python's `secrets` module for security-sensitive password generation.
- Add an option to guarantee that each selected character type appears in the password.
- Develop a graphical user interface.

## Author

Developed as part of the Oasis Infobyte Python Programming Internship.