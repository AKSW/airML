import os

JAR_EXECUTE = "java -jar kbox-v0.0.2-alpha.jar"  # kbox-v0.0.2-alpha.jar
SPACE = " "


def list(kns=False):
    """
    List all available models(kns=False) or list all KNS services(kns=True).
    :param kns: Define whether to list only the KNS services or not  :type boolean
    :return None
    :throws OSError
    """
    try:
        if kns:
            execute = JAR_EXECUTE + SPACE + "-list" + SPACE + "-kns"
        else:
            execute = JAR_EXECUTE + SPACE + "-list"
            os.system(execute)
    except OSError as e:
        raise OSError(e)


def install(modelUrl):
    """
    Install a given model by given URL.
    :param modelUrl: the url of the model to be installed :type string
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-install" + SPACE + modelUrl
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def installKNS(kns):
    """
    Install a given KNS service.
    :param kns: url of the kns service :type string
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-kns" + SPACE + kns
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def install(model, format=None, version=None, index=None, kns=None):
    """
    Install a given model base using the available KNS services to resolve it.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :param index: index of the model :type string
    :param kns: url of the kns service :type string
    :return None
    :throws OSError
    """
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + model
    try:
        if kns is not None:
            execute += (SPACE + "-kns" + SPACE + kns)
            if format is not None:
                execute += (SPACE + "-format" + SPACE + format)
        elif index is not None:
            execute += (SPACE + "-index" + SPACE + index)
        elif format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def removeKNS(kns):
    """
    Remove a given KNS service.
    :param kns: url of the kns service :type string
    :return None
    :throws OSError
    """
    execute = JAR_EXECUTE + SPACE + "-remove" + SPACE + "-kns" + SPACE + kns
    try:
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def getInfo(model, format=None, version=None):
    """
    Gives the information about a specific model.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError
    """
    execute = JAR_EXECUTE + SPACE + "-info" + SPACE + model
    try:
        if format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        return os.system(execute)
    except OSError as e:
        raise OSError(e)


def locate(model):
    """
    returns the local address of the given model.
    :param model: url of the model to be installed :type string
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + model
        return os.system(execute)
    except OSError as e:
        raise OSError(e)


def locate(model, format=None, version=None):
    """
    returns the local address of the given KB.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + + "-kb" + SPACE + model
        if format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        return os.system(execute)
    except OSError as e:
        raise OSError(e)


def search(pattern, format=None, version=None):
    """
    Search for all model-ids containing a given pattern.
    :param pattern: pattern of the url of the models
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-search" + SPACE + pattern
        if format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def getModelDirPath():
    """
    Show the path to the folder which contains the models.
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-r-dir"
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def setModelDirPath(dir):
    """
    Change the path of the resource folder.
    :param dir: new model path
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-r-dir" + SPACE + dir
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def showVersion():
    """
    display KBox version.
    :return None
    :throws OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-version"
        os.system(execute)
    except OSError as e:
        raise OSError(e)
