# Tax Calculator Project

## Made by:
- Mario Andrade Rojas
- Samuel Villa Carmona

## Objective 

The objective of this project is to develop a tax calculator that calculates the tax amount payable based on various income and expense parameters. The application will provide users an intuitive interface to input their incomes, payments, donations, among others, and it will show the result for the tax value. 


## How does it work?

The system will ask the person to enter some personal data and after that the person has to enter some information to calculate the tax: 
- Labor incomes
- Other Incomes, 
- Withholding sources
- Social Security Payments
- Pension Contributions
- Mortgage Payments 
- Donations
- Educational Expenses

Then the system will then handle the required calculations and provide the tax value.


## Main Folders:

### sql Folder
This file defines and creates the sql tables, including their relationships, data and types. This project has 3 tables:
- Income declaration 
- Natural Person
- Personal info

### src Folder

##### Console
File responsible for console interaction. It asks the user for their income and expenses and calculates taxes based on the values ​​entered.

#### Controller
This folder manages the database operations, handling tasks such as connecting to the database, executing queries, and processing data.

#### GUI
Core graphical user interface (GUI) file. Allows visual interaction with the user to enter data and display results.

#### TaxCalculator
Contains the main tax calculation logic, with the necessary formulas and rules.

### tests Folder
File containing unit tests (normal cases, extraordinary cases, and error cases) for tax calculations. Verifies the correct functioning of the defined formulas and logic.

There are also 3 files that belong to the project:
- .gitignore
- README.md 
- License

## How to Use?
## 1. Clone the Repository:
Open your command prompt and run the following command: 

git clone https://github.com/emmanuelcalad0615/CalculadoraImpuestos.git

## 2. Navigate to the Project Directory:
Change your directory to the CalculadoraImpuestos folder:

    cd path\to\CalculadoraImpuestos

*Example:* If you cloned the repository to C:\Projects, you would run:

    cd C:\Projects\CalculadoraImpuestos

### 3. Create a Virtual Environment

Before installing the required packages, it's recommended to create a virtual environment. Run the following commands:

#### Windows:

    py -m venv .venv
    .venv\Scripts\activate

#### macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

### 4. Install Requirements

Once the virtual environment is activated, install the required packages using the requirements.txt file:

    pip install -r requirements.txt

### 5. Execute the Program

#### Console Execution:

Run the console.py file:

    py src\Console\TaxCalculatorConsole.py

-When you run the program, you will be asked for some questios and the necessary information to calculate the tax value. Enter the numerical values ​​without commas, spaces or special characters (e.g. #$%&+-). The program will validate the data and, if everything is correct, it will calculate the amount of tax you should pay.

#### GUI Execution:

If a graphical user interface (GUI) is available, navigate to the GUI folder and run the TaxCalculatorGUI.py file:

    py src\GUI\TaxCalculatorGUI.py 

This folder contains the implementation of the project's graphical interface. The main file is Calculadora_gui.py, where the visual elements that allow the user to interact with the calculator in a more intuitive and user-friendly way are located.

This file uses Kivy's graphical libraries to create the window, buttons, and input fields needed to enter the user's data (income and expenses), and displays the result of the calculation on the screen
