from Scripts.Module import messageID, transkript, mayday, atemschutzdruck
import time

currentoperation = open("currentoperation.txt", "r")
operationpath = currentoperation.read()
currentoperation.close()

time.sleep(2)

while True:
    messageID.createid(operationpath)
    transkript.transkript(operationpath)
    mayday.mayday(operationpath)
    atemschutzdruck.druck(operationpath)
    time.sleep(1)
