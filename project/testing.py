import pandas as pd
import os




# Aktuelles Arbeitsverzeichnis erhalten
current_dir = os.getcwd()
#print(current_dir)

# Relativer Pfad zur AutomatedDataPipeline.py
relative_path_pipeline = "../data/AutomatedDataPipeline.py"
#pathtablefilter = "../data/tablefilter.py" 

# Absoluter Pfad berechnen
absolute_path = os.path.join(current_dir, relative_path_pipeline)
#absolute_path_filter = os.path.join(current_dir, pathtablefilter)
#Get the right paths
pathcar = "./CarRegistration.sqlite"
pathenergy = "./Energyprize.sqlite"
pathAutomatedDatapipeline = "./data/AutomatedDataPipeline.py"#pfad checken
print(os.path.abspath(pathAutomatedDatapipeline))
print("Filepath found")

    
#Run datapipeline
def runAutomatedDatapPipeline():
    command = "python " + os.path.abspath(absolute_path)
    os.system(command)
    
#Test path     
def testpipeline(path):
     assert os.path.exists(path)
    
    
    
def main():
    runAutomatedDatapPipeline()
    testpipeline(pathcar)
    testpipeline(pathenergy)
    print("Test completed")
    
if __name__ == "__main__":
    main()
    

    
    



 

