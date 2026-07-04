# Task 1: Introduction to Python Variables and Git

Welcome to your first task! In this assignment, you will learn the basics of Python variables, data types, and how to use Git to save and submit your code.

## 1. The Terminal
The terminal is a text-based interface used to interact with your computer. You will use it to run Python scripts and execute Git commands.

**How to open the terminal in VS Code:**
- **Menu:** Click on `Terminal` at the top of the window menu, then select `New Terminal`.
- **Keyboard Shortcut:** Press `` Ctrl + ` `` (Windows/Linux) or `` Cmd + ` `` (Mac).

## 2. Running a Python File
Once you have written your Python code in the `tasks` folder, you can run it to see the output. There are two ways to do this:
1. **The Play Button:** Open the Python file in VS Code and click the "Play" (▶) button in the top right corner of the editor window.
2. **The Terminal:** Open the terminal and type the following command, then press Enter:
   ```bash
   python tasks/task_1.py
   ```

## 3. Git Basics
Git is a version control system that tracks changes to your code and allows you to share it. Here are the essential commands you need to know for this course:

- `git status`: Shows the state of your working directory. It tells you which files have been modified or are ready to be saved.
- `git add <file_name>`: Stages a specific file, preparing it to be saved (committed). For example, `git add tasks/task_1.py`.
- `git add *` or `git add .`: Stages *all* modified files at once.
- `git commit -m "message"`: Saves your staged changes with a short, descriptive message explaining what you did. E.g., `git commit -m "Completed Task 1"`.
- `git fetch`: Downloads new data from the remote repository (like GitHub) without integrating it into your local files.
- `git pull`: Downloads new data and immediately integrates (merges) it into your local files.
- `git push`: Uploads your local commits to the remote repository so others (like your instructor) can see your work.

## 4. Your Assignment
1. Open the file `tasks/task_1.py`.
2. Read through the examples provided in the file to learn about data types and variables.
3. Complete the `TODO` sections by writing your own Python code.
4. Run your code using the Play button or the terminal to make sure it works!
5. When you are finished, use the terminal to submit your work to your instructor:
   ```bash
   git status
   git add tasks/task_1.py
   git commit -m "Finished task 1"
   git push
   ```
