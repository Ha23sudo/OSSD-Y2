  Course Repository – Weekly Lab & Tasks

Welcome to the official course repository. This repository will be updated **every week during class sessions** with new code examples and tasks.


 Objective

* Follow along with in-class coding
* Practice concepts after class
* Maintain your own copy of the work
* Submit weekly progress (if required)

Weekly Workflow (IMPORTANT)

Follow these steps **every week**:

### 1. Fork the Repository (ONLY ONCE)

* Click the **Fork** button on the top right
* This creates your own copy of the repository


### 2. Clone Your Fork

bash
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME


### 3. Add Upstream (ONLY ONCE)

This connects your repo to the original course repo.

bash
git remote add upstream https://github.com/TEACHER-USERNAME/REPO-NAME.git

### 4. Every Week – Get Latest Updates

Before starting work each week:

bash
git pull upstream main


If this fails, use:

bash
git fetch upstream
git merge upstream/main

### 5. Work on Weekly Tasks

* Navigate to the folder for the current week
* Complete the given tasks
* Modify or create files as required

### 6. Commit Your Work

bash
git add .
git commit -m "Week X - Task completed"


### 7. Push to Your Fork

bash
git push origin main


##  Repository Structure

/Week-09
/Week-10
/Week-11
...
README.md
Each Week folder will contain the tasks to be completed most probably the one we started in the class session.

## ⚠️ Important Rules

* ❌ Do NOT push directly to the main course repository
* ✅ Always work on your fork
* ❌ Do NOT delete or modify original class files unnecessarily
* ✅ Add your solutions in separate files if instructed



##  Tips for Success

* Pull updates **before every class**
* Keep commits clean and meaningful
* Ask questions if you get stuck


##  Notes

* New content will be added weekly during class
* Instructions for each week will be inside respective folders
* Make sure your repository is always up-to-date

---

