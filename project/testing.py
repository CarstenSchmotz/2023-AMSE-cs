import pandas as pd
import os


pathcar = "./CarRegistration.sqlite"
pathenergy = "./Energyprize.sqlite"
pathAutomatedDatapipeline = "./AutomatedDataPipeline.py"
print(os.path.abspath(pathAutomatedDatapipeline))
print("Filepath found")

    

def runAutomatedDatapPipeline():
    command = "python " + os.path.abspath(pathAutomatedDatapipeline)
    os.system(command)
    
def testpipeline(path):
     assert os.path.exists(path)
    
    
    
def main():
    runAutomatedDatapPipeline()
    testpipeline(pathcar)
    testpipeline(pathenergy)
    print("Test completed")
    
if __name__ == "__main__":
    main()
    

    
    



 

