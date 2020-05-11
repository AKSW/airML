import sys
import os
    
JAR_EXECUTE = "java -jar kbox.jar" # kbox-v0.0.2-alpha.jar
SPACE = " "

#Create an index with the files in a given directory.
def createIndex(dir):
    execute = JAR_EXECUTE + SPACE + "-createIndex" + SPACE + dir
    os.system(execute)
    return


# Serialize the content of a directory to be served in a KNS system.
def serialize(dir):
    execute = JAR_EXECUTE + SPACE + "-serialize" + SPACE + dir 
    os.system(execute)
    return

def sparql(query):
    return

# Start an SPARQL enpoint in the given subDomain containing the given KB.
def server(port="8080",subDomain="kbox",kb):
    execute = JAR_EXECUTE + SPACE + "-server" + SPACE + "-port" + SPACE + port + SPACE + "-subdomain" + SPACE + subDomain + SPACE + "-kb" + SPACE + kb + SPACE +"-install"
    return os.system(execute)

# List all available knowledge base.
# List all availables KNS services.
def showList(kns=False):
    if kns:
        execute = JAR_EXECUTE + SPACE + "-list" + SPACE + "-kns"  + SPACE + kns
    else:
        execute = JAR_EXECUTE + SPACE + "-list"
    return os.system(execute)

# Install a given resource.
def installByUrl(url):
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + url
    os.system(execute)

# Install a given KNS service.
def installKNS(kns):
    execute = JAR_EXECUTE + SPACE + "-kns" + SPACE + kns
    os.system(execute)

# Install a given knowledge base using the available KNS services to resolve it.
def installKB(kb,format=None,version=None,index=None,kns=None):
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + kb
    if kns!=None:
        execute+=(SPACE + "-kns" + SPACE + kns)
        if format!=None:
            execute+=(SPACE + "-format" + SPACE + format)
    elif index!=None:
        execute +=(SPACE + "-index" + SPACE + index)
    elif format!=None:
        execute+=(SPACE + "-format" + SPACE + format)
        if version!=None:
            execute+=(SPACE + "-version" + SPACE + version)
    os.system(execute)

# Remove a given KNS service.
def removeKNS(kns):
    execute = JAR_EXECUTE + SPACE + "-remove" + SPACE + "-kns" + SPACE + kns
    os.system(execute)

# Gives the information about a specific KB.
def getInfo(url,format=None,version=None):
    execute = JAR_EXECUTE + SPACE + "-info" + SPACE + url
    if format!=None:
        execute+=(SPACE + "-format" + SPACE + format)
        if version!=None:
            execute+=(SPACE + "-version" + SPACE + version)
    return os.system(execute)

# returns the local address of the given resource.
def locateResource(url):
    execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + url
    return os.system(execute)

# returns the local address of the given KB.
def locateKB(url,format=None,version=None):
    execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + + "-kb" + SPACE + url
    if format!=None:
        execute+=(SPACE + "-format" + SPACE + format)
        if version!=None:
            execute+=(SPACE + "-version" + SPACE + version)
    return os.system(execute)

# Search for all kb-URL containing a given pattern.
def search(pattern,format=None,version=None):
    execute = JAR_EXECUTE + SPACE + "-search" + SPACE + pattern
    if format!=None:
        execute+=(SPACE + "-format" + SPACE + format)
        if version!=None:
            execute+=(SPACE + "-version" + SPACE + version)
    os.system(execute)

# Show the path to the resource folder.
def getResourceDirPath():
    execute = JAR_EXECUTE + SPACE + "-r-dir"
    os.system(execute)

# Change the path of the resource folder.
def changeResourceDirPath(dir):
    execute = JAR_EXECUTE + SPACE + "-r-dir" + SPACE + dir
    os.system(execute)

# display KBox version.
def showVersion():
    execute = JAR_EXECUTE + SPACE + "-version"
    return os.system(execute)
