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

## Prerequisites & Installation

To run these scripts, you must install Python 3.x and the ANTLR4 Python runtime engine.

1. **Install ANTLR4 Runtime for Python:**
```bash
   pip install antlr4-python3-runtime
