# Bank With Python (GUI)

## Project Info
**Name**: Bank With Python (GUI)\
**Purpose**: To Create A Bank Management System Using Python and Tkinter\
**Author**: Virati Akira Nandhan Reddy\
**Email**: viratiaki29@gmail.com

This project is a GUI-based banking application built using Python. It provides a wide range of functionalities for managing user accounts, transactions, and other banking operations. The application is designed to be user-friendly and secure, making it suitable for educational purposes and small-scale banking systems.

---

## Features
The application includes the following features:
1. **Login Screen**: Secure user authentication with password validation.
2. **Create Account**: Allows users to create new accounts with unique security codes.
3. **Deposit Money**: Enables users to deposit money into their accounts.
4. **Withdraw Money**: Allows users to withdraw money securely.
5. **Transfer Money**: Facilitates money transfers between accounts.
6. **Check Balance**: Displays the current balance of the user's account.
7. **Update Account**: Provides options to update user details.
8. **Delete Account**: Allows users to delete their accounts permanently.
9. **View All Accounts**: Displays a list of all accounts for administrative purposes.
10. **Logout**: Securely logs out the user from the application.

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:
1. **Python**: Version 3.13.0 (64-Bit) or higher.
2. **Pip**: Python package manager.
3. **Git**: For cloning the repository.

---

## Installation
Follow these steps to set up the project on your local machine:

### Step 1: Clone the Repository
Clone the repository from GitHub using the following command:
```bash
git clone https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities.git
```

### Step 2: Navigate to the Project Directory
Change your working directory to the project folder:
```bash
cd Bank-With-High-Functionalities
```

### Step 3: Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
Ensure all dependencies are installed correctly by running:
```bash
python -m pip check
```

---

## Usage
### Running the Application
To start the application, execute the following command:
```bash
python Main_Bank.py
```

### Navigating the GUI
1. **Login**: Enter your username and password to access your account.
2. **Create Account**: If you are a new user, create an account by providing the required details.
3. **Perform Transactions**: Use the options provided in the user interface to deposit, withdraw, or transfer money.
4. **Logout**: Securely log out after completing your tasks.

---

## External Modules
The project uses the following external Python modules:
1. **`customtkinter`**: For creating modern and customizable GUI components.
2. **`importlib`**: For dynamic imports and module management.
3. **`os`**: For file and directory operations.
4. **`pillow (PIL)`**: For handling image processing tasks.

---

## File Structure
The project is organized as follows:
```
Bank-With-High-Functionalities/
│
├── Bank_Package/
│   ├── __init__.py
│   ├── Login_Screen.py
│   ├── Create_Account.py
│   ├── Product_Activation.py
│   ├── User_Actions.py
│   ├── Gmail/
│   │   ├── __init__.py
│   │   ├── Gmail History.txt
│   │   ├── Login Credentials.json
│   ├── ...
│
├── Main_Bank.py
├── requirements.txt
├── LICENSE
├── README.md
├── ...
```

---

## Contribution Guidelines
We welcome contributions to improve this project. To contribute:
1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them with a descriptive message:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

---

## Known Issues
- **Data Integrity**: Ensure that critical files like `Data_Of_User.txt` and `Gmail History.txt` are not deleted or modified manually.
- **Compatibility**: The application is tested on Python 3.13.0. Compatibility with older versions is not guaranteed.

---

## Owner Info
The whole script is written in Python.\
**Python Version Used**: 3.13.0 (64-Bit)\
**Code Editor Used**: Microsoft's Visual Studio Code

**Owner**: Virati Akira Nandhan Reddy\
**Contact Me At**:\
- **Email**: viratiaki29@gmail.com\
- **Instagram**: [viratiaki53](https://www.instagram.com/viratiaki53/)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
Special thanks to:
- The Python community for providing extensive libraries and documentation.
- Contributors who helped improve the project.
- Users who provided feedback for enhancements.
