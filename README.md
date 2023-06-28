# AMSE/SAKI 2023 Template Project
This a open data project in the AMSE/SAKI module for FAU in data engineering.
This repository contains a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.


# Project Setup
The following files are part of this project:

- `data.sqlite`: The final, cleaned dataset. 

- `exploration.ipynb`: A Jupyter notebook that you can use to explore your data and show in detail what it looks like. You can refer to this file in your report for users that want more information about your data.
- `report.ipynb`: Your final report as a Jupyter notebook. This is the result of your project work and should lead with a question that you want to answer using open data. The content of the report should answer the question, ideally using fitting visualizations, based on the data in `data.sqlite`.

- `Project Folder`:

	- `AutomatedDataPipeline.py`: Automated data pipeline to get the data.
	- `needed.txt`: A textfile to get the requirments for the test.
	- `testing.py`: The test file which test the pipeline and codepaths of sql databases.
	- `testing.sh`: A shell script ot start the test file.
	- `project-plan.md`: The organistion file for the project.
	- `gitignore`: Prevents that `.sql` files get summited online to github in order to prevent storage shortage.

# Manual

-First of all am automated data pipeline `AutomatedDataPipeline.py` downloads the relevant data from the internet. 
-The second part is to filter the Datatables with `tablefilter.py` which deleted redundant data. The tables are reduced to the summary of the year and the rows are inverse so that the data sets fits each other.  
-Lastly the data is stored in `data.sqlite` for the exploration and the report.
- These files are automatically enabled in the report.

# Adtional
Github actions are enabled to test the pipeline on every push. This ensures that the data is downloaded correctly.
github/workflows' folder:
`continuous_integration.yml`: Starts the Github pipeline action test.
`exercise-feedback.yml`: Enables grading for the exercises.


# Exercises
The exercises folder in the repository contains the results of the exercises that were completed throughout the semester. Exercises one, three, and five are completed in Jayvee, while exercises two and four are completed in Python. Github actions are used to test and grade the exercises.

