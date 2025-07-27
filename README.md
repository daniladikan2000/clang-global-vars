# 🔍 C++ Global Variable Analyzer

This is a simple Python script that uses **Clang's AST** to automatically find **global variables** in C++ source files.

The script parses all `.cpp` files in the `cpp_sources/` directory and saves the names of global variables into `output.txt`.

---

## 📦 Features

- Parses C++ code using Clang AST
- Detects global variables by analyzing AST structure
- Works on multiple `.cpp` files
- Outputs results to a plain text file

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/clang-global-vars.git
   cd clang-global-vars
   
2. Install Python bindings for Clang:

   ```bash
   pip install clang
   ```

3. Install LLVM and Clang if not already installed:

   ```bash
   sudo apt install libclang-dev llvm
   ```

4. Put your `.cpp` files into the `cpp_sources/` directory.

5. Run the script:

   ```bash
   python3 main.py
   ```

6. Check the results in `output.txt`.

---

## 🔧 Project Structure

```
clang-global-vars/
├── main.py          # Main analysis script
├── cpp_sources/     # Folder with C++ files to analyze
├── output.txt       # Output file (auto-generated)
└── README.md
```

---

## 📚 Useful Resources

* [🔗 Clang Libraries Lecture Slides (PDF)](https://github.com/mdadams/clang_libraries_companion/releases/download/v0.3.0/lecture_slides_for_the_clang_libraries-0.3.0.pdf)
  A helpful presentation explaining how to use Clang's libraries and AST in practice.


