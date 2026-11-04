# Cybersecurity Password Tool

A small, simple application written in Python that creates cryptographically secure, random passwords and checks password submission for compliance with minimal security standards.

## Features
* **Guaranteed Complexity:** The generator ensures at least one uppercase letter, one lowercase letter, one digit, and one special character are included.
* **Array Shuffling:** Uses Python's `random.shuffle` to eliminate predictable character placement patterns.
* **Strength Assessment:** Evaluates inputs based on length and character variance, providing actionable feedback to the user.

## Future Enhancements
* Transition from `random` to the `secrets` module for true cryptographically secure pseudorandom number generation (CSPRNG).
* Implement a local graphical user interface (GUI) or deploy as a web app.
