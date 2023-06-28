# AMSE/SAKI 2023 Template Project
This is an open data project in the AMSE/SAKI module for FAU in Data Engineering.
This repository contains a data science project developed by the student over the course of the semester, and (b) the exercises submitted over the course of the semester.


# Project Setup
The following files are included in this project

- `data.sqlite`: The final, cleaned dataset. 

- exploration.ipynb: A Jupyter notebook you can use to explore your data and show how it looks in detail. You can refer to this file in your report for users who want more information about your data.
- report.ipynb: Your final report as a Jupyter notebook. This is the result of your project work and should start with a question you want to answer using open data. The content of the report should answer the question, ideally using appropriate visualizations, based on the data in `data.sqlite`.

- Project Folder:

	- AutomatedDataPipeline.py: Automated data pipeline to retrieve the data.
	- `needed.txt`: A text file to get the requirements for the test.
	- `testing.py`: The test file that tests the pipeline and codepaths of sql databases.
	- `testing.sh`: A shell script to run the test file.
	- `project-plan.md`: The organization file for the project.
	- gitignore: Prevents `.sql' files from being uploaded online to github, to avoid memory shortage.

# Manual

-First, an automated data pipeline `AutomatedDataPipeline.py` downloads the relevant data from the internet. 
-The second part is to filter the datatables with `tablefilter.py`, which deletes redundant data. The tables are reduced to the summary of the year and the rows are inverted so that the datasets match.  
-Finally, the data is stored in `data.sqlite` for exploration and the report.
- These files are automatically activated in the report.

# Additional
Github actions are enabled to test the pipeline on every push. This ensures that the data is downloaded correctly.
github/workflows' folder:
`continuous_integration.yml`: Launches the Github pipeline action test.
`exercise-feedback.yml`: Enables grading for the exercises.

# Exercises
The exercises folder in the repository contains the results of the exercises that were completed throughout the semester. Exercises one, three, and five are completed in Jayvee, while exercises two and four are completed in Python. Github actions are used to test and grade the exercises.

