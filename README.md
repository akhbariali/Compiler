# ANTLR-Based Source Code Refactoring and Analysis Tools

This project implements a collection of abstract syntax tree (AST) source code manipulation and analysis tools using **Python** and **ANTLR**. The tools automate structural transformations, boilerplate code generation, abstract method implementation, and syntax validation for object-oriented program code.

---

## Project Overview

The repository contains solutions to four distinct compiler/source-to-source translation assignments:

| Module | Description | Key Mechanism |
| :--- | :--- | :--- |
| **Task 1: Encapsulation Helper** | Detects private fields and automatically generates standard public `getter` and `setter` methods. For `final` (constant) fields, it intelligently generates only the `getter`. | ANTLR AST Listener / Rewrite |
| **Task 2: Interface Stubber** | Scans for empty method bodies (unimplemented methods) and automatically injects a `throw new UnsupportedOperationException();` instruction. | Token Stream Editing |
| **Task 3: Try-Catch Guard** | Analyzes `try-catch` structures. If a global/general `Exception` block is missing down the block chain, it safely appends a default catch block to log the error message. | Conditional Node Injection |
| **Task 4: Optional Parameter Logger**| Identifies functions containing optional/default arguments and saves the default values into a separate structured format template: `<function_name>_default_param`. | Symbol Extraction |

---

## Technologies Used

* Python 3
* ANTLR4
* Java Grammar (Lexer & Parser)

---

## How It Works

The parser traverses Java class declarations and identifies private field declarations.

For each field:

* A getter method is generated
* A setter method is generated unless the field is declared as `final`

---

## Running the Project

### Install ANTLR Runtime

```bash
pip install antlr4-python3-runtime
```

### Run

```bash
python main.py
```

The transformed source code will be written to:

```text
output.java
```

---

## Educational Purpose

This project demonstrates:

* Parsing techniques
* Abstract syntax tree traversal
* Source-to-source transformation
* Compiler construction fundamentals
* Code generation automation


# Java Empty Method Guard

A Java source transformation tool that detects empty method bodies and automatically inserts `UnsupportedOperationException` placeholders using Python and ANTLR4.

## Features

* Parses Java source code
* Detects empty methods:

  ```java
  {}
  ```
* Replaces empty implementations with:

  ```java
  throw new UnsupportedOperationException();
  ```
* Helps prevent silent unfinished implementations

---

## Technologies Used

* Python 3
* ANTLR4
* Java Parser Grammar

---

## How It Works

The parser traverses Java method declarations and checks whether the method body is empty.

If an empty body is detected, the tool injects:

```java
throw new UnsupportedOperationException();
```

This makes unfinished methods explicit during runtime.

---

## Running the Project

### Install Dependencies

```bash
pip install antlr4-python3-runtime
```

### Execute

```bash
python main.py
```

Generated output will be saved in:

```text
output.java
```

---

## Educational Purpose

This project demonstrates:

* Parse tree traversal
* Java code transformation
* Token stream rewriting
* Static code analysis concepts
* Compiler construction basics


# Java Exception Catch Injector

A source-to-source Java transformation tool that automatically injects generic exception handlers into `try-catch` blocks using Python and ANTLR4.

## Features

* Parses Java source code
* Detects `try-catch` statements
* Verifies whether a generic:

  ```java
  catch(Exception e)
  ```

  handler exists
* Automatically appends a fallback exception handler if missing

---

## Technologies Used

* Python 3
* ANTLR4
* Java Grammar Parser

---

## How It Works

The parser analyzes all `try-catch` blocks and inspects existing catch clauses.

If no generic exception handler is found, the tool injects:

```java
catch(Exception e) {
    System.out.println("Exception message: " + e.getMessage());
}
```

This provides a fallback handler for uncaught exceptions.

---

## Running the Project

### Install Dependencies

```bash
pip install antlr4-python3-runtime
```

### Run

```bash
python main.py
```

The transformed Java source code will be written to:

```text
output.java
```

---

## Educational Purpose

This project demonstrates:

* Compiler design concepts
* Java parsing
* Source code rewriting
* Exception handling augmentation
* Parse tree manipulation using ANTLR4
