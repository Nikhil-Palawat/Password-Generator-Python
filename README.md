# Password-Generator-Python
Random Password Generator with Python
A simple and secure password generator written in Python. This program creates strong and random passwords, suitable for securing online accounts, databases, or any application where security is a priority.

## Features
Generates passwords of length 12 (default).
  
  
  Ensures inclusion of:
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number
- At least 1 special character
- Randomly shuffles characters to avoid predictable patterns.
- Lightweight and easy to use.

### Requirements :
Python 3.6 or later

Installation :
Clone the repository or download the script directly:

```python
git clone https://github.com/Nikhil-Palawat/Password-Generator-Python.git
cd Password-Generator-Python
```
Ensure Python is installed on your system. You can check your Python version by running:
```python
python --version
```

## Usage
- Run the script using Python:
```python
python password_generator.py
```
- The script will generate and display a random password in the terminal.

## Example
Here’s an example of generating a password:
```
Generated Password: G7$y3B&kLp8D
```

## Customization
To change the password length, modify the length parameter in the generate_password function call. 

For example:
```
print("Generated Password:", generate_password(length=16))
```

## Security
- The generated passwords are random and designed for high security.
- Ensure the script is run on a trusted environment to prevent potential security risks.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

## License
This project is licensed under the GNU General Public License v3.0.

You are free to use, modify, and distribute this software, provided you adhere to the terms of the GPLv3.
