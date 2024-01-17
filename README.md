# 🧐 Regular Expression Character Checker

## 📝 Assignment Overview

This programming assignment focuses on creating a user input validator for regular expressions. The acceptable input includes zero or more characters from the alphabet of {a, b, +, *, (, )} (or the alphabet of your choice, which should include the elementary regular expression operators of {+, *, (, )}).

### 📋 Requirements

1. Allow users to enter multiple lines of "words" from the console.
2. Each word is delimited by a carriage return or a maximum of 1,000 characters.
3. Blanks or tabs should be ignored during input processing.
4. Display each word along with an indication of whether it consists of valid characters.
5. Identify and display any invalid characters in the word.
6. Terminate the program when the user enters an empty word (a blank line).

### 🚀 Example Run

```bash
Regular expression validator over the alphabet {a, b, +, *, (, )}

Enter regular expression: ab
**✅ VALID:** ab

Enter regular expression: ab ( ba)*
**✅ VALID:** ab(ba)*

Enter regular expression: ab ( ba)*X+ba ( bb
**❌ INVALID:** ab(ba)*X+ba(bb
^

Enter regular expression: ) & 0 # $ b ( - b a)*X+ba ( bb
**❌ INVALID:** )&a#$b(-ba)*X+ba(bb
^ ^^ ^ ^

<blank line>
Program terminated.
```

### 🛠️ Implementation Guidelines

- Design the program for future extensions with a minimal amount of unessential complexity.
- Allow for the addition of expression processing functionality in future assignments.

### 📤 Solution Submission

- Submit the solution in a convenient package.
- Include properly documented source code.
- Provide an executable if appropriate.

### 🌐 GitHub Repository

[**GitHub Repository**](https://github.com/ANUJDWIVDI/inputvalidator_assign)
