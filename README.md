# Neel – Python Personal Assistant 🤖

A simple **command-line personal assistant written in Python**.
This program interacts with the user, validates basic details, and provides small utilities such as a **calculator** and a **rock-paper-scissors game**.

The assistant introduces itself as **Neel** and was created by **Noel**.

---

## Features

### 👤 User Information

The assistant asks the user for:

* First name
* Age
* Height (in cm)

It validates the input to ensure:

* The name contains only letters.
* Age is a valid number.
* Height is a valid number.

---

### ✅ User Validation

Access to the assistant depends on:

* Age must be **18 or above**
* Height must be **170 cm or more**
* Age must be **below 100**

If the user does not meet these requirements, the program exits.

---

### 🧮 Calculator

The built-in calculator supports:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation

The program validates numeric input before performing calculations.

---

### 🎮 Rock, Paper, Scissors

A simple game where:

* The user chooses **rock**, **paper**, or **scissors**
* The computer randomly selects a choice
* The program determines the winner

---

### 📋 Main Menu

After validation, users can choose from the following options:

1. Who are you?
2. Who made you?
3. What are you made for?
4. Calculator
5. Rock, Paper, Scissors

The program continues running until the user chooses to exit.

---

## How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check with:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/neel-assistant.git
cd neel-assistant
```

---

### 3. Run the Program

```bash
python assistant.py
```

---

## Example Flow

```
I am your personal assistant.
What is your name?
Noel

How old are you?
18

What is your height (cm)?
175

Hello Noel, aged 18 and 175cm tall!
You are an adult and meet the height requirement.

This is a list of functions:
1. Who are you?
2. Who made you?
3. What are you made for?
4. Calculator
5. Rock, Paper, Scissors
```

---

## Project Structure

```
assistant.py
README.md
```

* **assistant.py** → Main program containing all functions
* **README.md** → Project documentation

---

## Technologies Used

* Python 3
* Built-in Python libraries:

  * `random`

---

## Author

**Noel**

---

## License

This project is open-source and free to use.
