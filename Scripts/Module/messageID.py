import re


# Erstellt einen hash aus dem Pfad der NAchricht
def createid(operationpath):
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    todo = re.findall("<!-- messageid -->.*", guitxt)
    if len(todo) == 0:
        print("Alle Module verarbeitet")
    else:
        for x in range(len(todo)):
            print("messageID" + str(todo[x]))
            hashid = re.sub("<!-- messageid --><!-- | -->", "", todo[x])
            guitxt = re.sub("<!-- messageid -->", "ID =  " + str(hex(hash(hashid))), guitxt, 1)

        gui = open(operationpath + "/GUI.html", "w")
        gui.write(guitxt)
        gui.close()


