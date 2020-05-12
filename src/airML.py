import os

JAR_EXECUTE = "java -jar kbox-v0.0.2-alpha.jar"  # kbox-v0.0.2-alpha.jar
SPACE = " "

def list(kns=False):
    """
    List all available models(kns=False) or list all KNS services(kns=True).
    :param kns: boolean
    :return:
    """
    if kns:
        execute = JAR_EXECUTE + SPACE + "-list" + SPACE + "-kns"
    else:
        execute = JAR_EXECUTE + SPACE + "-list"
    return os.system(execute)

def install(modelUrl):
    """
    Install a given model.
    :param modelUrl: the url of the model to be installed :type string
    """
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + modelUrl
    os.system(execute)


# Install a given KNS service.
def installKNS(kns):
    """
    Install a given KNS service.
    :param kns: url of the kns service :type string
    """
    execute = JAR_EXECUTE + SPACE + "-kns" + SPACE + kns
    os.system(execute)

def install(model, format=None, version=None, index=None, kns=None):
    """
    Install a given model base using the available KNS services to resolve it.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :param index: index of the model :type string
    :param kns: url of the kns service :type string
    """
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + model
    if kns != None:
        execute += (SPACE + "-kns" + SPACE + kns)
        if format != None:
            execute += (SPACE + "-format" + SPACE + format)
    elif index != None:
        execute += (SPACE + "-index" + SPACE + index)
    elif format != None:
        execute += (SPACE + "-format" + SPACE + format)
        if version != None:
            execute += (SPACE + "-version" + SPACE + version)
    os.system(execute)


# Remove a given KNS service.
def removeKNS(kns):
    """

    :param kns:
    """
    execute = JAR_EXECUTE + SPACE + "-remove" + SPACE + "-kns" + SPACE + kns
    os.system(execute)


# Gives the information about a specific model.
def getInfo(model, format=None, version=None):
    execute = JAR_EXECUTE + SPACE + "-info" + SPACE + model
    if format != None:
        execute += (SPACE + "-format" + SPACE + format)
        if version != None:
            execute += (SPACE + "-version" + SPACE + version)
    return os.system(execute)


# returns the local address of the given resource.
def locate(model):
    execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + model
    return os.system(execute)


# returns the local address of the given KB.
def locate(model, format=None, version=None):
    execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + + "-kb" + SPACE + url
    if format != None:
        execute += (SPACE + "-format" + SPACE + format)
        if version != None:
            execute += (SPACE + "-version" + SPACE + version)
    return os.system(execute)


# Search for all model-id containing a given pattern.
def search(pattern, format=None, version=None):
    execute = JAR_EXECUTE + SPACE + "-search" + SPACE + pattern
    if format != None:
        execute += (SPACE + "-format" + SPACE + format)
        if version != None:
            execute += (SPACE + "-version" + SPACE + version)
    os.system(execute)


# Show the path to the folder which contains the models.
def getModelDirPath():
    execute = JAR_EXECUTE + SPACE + "-r-dir"
    os.system(execute)


# Change the path of the resource folder.
def setModelDirPath(dir):
    execute = JAR_EXECUTE + SPACE + "-r-dir" + SPACE + dir
    os.system(execute)


# display KBox version.
def showVersion():
    execute = JAR_EXECUTE + SPACE + "-version"
    return os.system(execute)
