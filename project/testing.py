import pandas as pd
import os

#Get the right paths
pathcar = "./CarRegistration.sqlite"
pathenergy = "./Energyprize.sqlite"
pathAutomatedDatapipeline = "./AutomatedDataPipeline.py"
print(os.path.abspath(pathAutomatedDatapipeline))
print("Filepath found")

    
#Run datapipeline
def runAutomatedDatapPipeline():
    command = "python " + os.path.abspath(pathAutomatedDatapipeline)
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
    

    
    



 

