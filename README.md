# JSON Parser Implementation

This repository contains an implementation of a JSON parser, developed as part of a coding challenge from [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-json-parser). The project is structured with each development step in its own branch, following a step-by-step approach.

## Challenge Overview

The challenge involves building a JSON parser from scratch, which is an excellent way to understand parsing techniques applicable to various domains, from simple data formats to complex compilers. The process is typically divided into two main stages:

1. **Lexical Analysis**: Breaking down a sequence of characters into meaningful tokens.
2. **Syntactic Analysis**: Analyzing these tokens to match a formal grammar.

For more details on the challenge, visit the [Coding Challenges website](https://codingchallenges.fyi/challenges/challenge-json-parser).

## Project Structure

The project is organized with each step of the development process in its own branch. This structure allows for a clear progression and understanding of the parser's development. The main components include:

- **`parser.py`**: Contains the main parsing logic.
- **`helper.py`**: Includes utility functions to support the parser.
- **`constants.py`**: Defines constants used throughout the project.
- **`tests/`**: Directory containing test cases to validate the parser's functionality.

## Getting Started

To get a local copy of the project up and running, follow these steps:

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MehrShahbaz/CoddingChallange-2.git
   cd CoddingChallange-2
   ```

2. **Checkout the desired branch**:

   The project is structured with each step in its own branch. To view a specific step:

   ```bash
   git checkout step-<number>
   ```

   Replace `<number>` with the step number you're interested in.

3. **Install dependencies**:

   If there are any dependencies, install them using:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: Ensure you have a `requirements.txt` file listing all necessary packages.*

## Usage

To run the JSON parser:

```bash
python parser.py <input_file>
```

Replace `<input_file>` with the path to the JSON file you wish to parse.

## Running Tests

To execute the test suite and verify the parser's functionality:

```bash
python -m unittest discover tests/
```

This command will discover and run all test cases in the `tests/` directory.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-json-parser) for providing the challenge and resources.