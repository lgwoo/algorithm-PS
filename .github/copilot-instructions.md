# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace is a collection of algorithm problem solutions, primarily in Python, organized by difficulty and problem number. Each file typically solves a single problem, often from online judges (e.g., Baekjoon, Programmers).

## Directory Structure
- `pycoding_ago/`: Main directory for Python solutions. Filenames encode problem level, number, and sometimes the problem name (e.g., `G4_14500_테트로미노.py`).
- `dreamhack/`: Contains non-Python files and some JavaScript (e.g., `main.js`).
- `D2CodingAll/`: Font files, not code.

## Key Conventions
- **File Naming**: Python files are prefixed with the problem level (e.g., `B1`, `G4`, `S1`), followed by the problem number and name. This helps with quick identification and sorting.
- **Single-File Solutions**: Each `.py` file is a self-contained solution. There is no shared library or cross-file import pattern.
- **No Central Entry Point**: There is no main application or build process. Each file is intended to be run independently.
- **Minimal External Dependencies**: Solutions use only the Python standard library. Do not add external dependencies unless absolutely necessary for a specific problem.

## Developer Workflows
- **Running Solutions**: Run any solution directly with Python 3 (e.g., `python S1_1992_쿼드트리.py`).
- **Testing**: There is no unified test suite. Test each solution by providing input as specified in the problem statement (usually via stdin).
- **Debugging**: Add print statements or use a debugger as needed. No project-wide debugging tools are configured.

## Patterns and Practices
- **Input Handling**: Most files use `sys.stdin.readline` or `input()` for reading input. Avoid hardcoding input unless for local testing.
- **Output**: Print results directly to stdout.
- **Comments**: Use comments to clarify tricky logic, especially for non-trivial algorithms.
- **Korean Filenames/Comments**: Some files and comments are in Korean. Preserve this for consistency.

## Examples
- See `pycoding_ago/S1_1992_쿼드트리.py` for a typical problem solution structure.
- See `pycoding_ago/G4_14500_테트로미노.py` for a more complex algorithmic solution.

## What NOT to Do
- Do not refactor solutions into shared modules unless explicitly requested.
- Do not introduce new dependencies or frameworks.
- Do not change file naming conventions.

---
For questions or unclear conventions, ask for clarification before making large-scale changes.
