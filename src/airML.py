import os
import subprocess

DEFAULT_KNS = ""
JAR_EXECUTE = "java -jar kbox-v0.0.2-alpha.jar"  # kbox-v0.0.2-alpha.jar
SPACE = " "


def list(kns=False):
    """ List all available models(kns=False) or list all KNS services(kns=True).
    Args:
      kns:'boolean',defines whether to list only the KNS services or not
    Returns:
        None
    Throws:
        OSError
    """
    try:
        if kns:
            execute = JAR_EXECUTE + SPACE + "-list" + SPACE + "-kns"
        else:
            execute = JAR_EXECUTE + SPACE + "-list"
            os.system(execute)
    except OSError as e:
        print(OSError(e))


def install(modelID, format=None, version=None):
    """ Install the a model by given modelID
    Args:
        modelID: 'string', url of the model hosted in a public repository.
        format:  'string', format of the model.
        version: 'string' specific version to be installed of the the model.
    Returns:
        None
    Throws:
        OSError
    Example:
        install("http://github.org/aksw/NSpM/monument_300","NSPM/Model","0")
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + modelID
        if format is not None:
            execute += (SPACE + "-format" + SPACE + format)
        elif format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        execute += (SPACE + "-kns" + SPACE + DEFAULT_KNS)
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def install(modelID, format=None, version=None, kns=None):
    """ Install a given model base using the available KNS services to resolve it.
    Args:
        modelID:'string',url of the model to be installed.
        format: 'string',format of the model.
        version:'string',version of the model.
        kns:'string', url of the kns service.
    Returns:
        None
    Throws:
        OSError
    """
    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + modelID
    try:
        if kns is not None:
            execute += (SPACE + "-kns" + SPACE + kns)
            if format is not None:
                execute += (SPACE + "-format" + SPACE + format)
        elif format is not None:
            execute += (SPACE + "-format" + SPACE + format)
            if version is not None:
                execute += (SPACE + "-version" + SPACE + version)
        os.system(execute)
    except OSError as e:
        raise OSError(e)


# def install(modelID, model,format, version):
#     # TODO: Have to implement the function
#     return


def removeKNS(kns):
    """ Remove a given KNS service.
    Args:
        kns:'string', url of the kns service.
    Returns:
        None
    Throws:
        OSError
    """
    execute = JAR_EXECUTE + SPACE + "-remove" + SPACE + "-kns" + SPACE + kns
    try:
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def getInfo(model, format=None, version=None):
    """ Gives the information about a specific model.
    Args:
        model: url of the model to be installed.
        format: format of the model.
        version: version of the model.
    Return:
        None
    Throws:
        OSError
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
    """ Find the local address of the given model.
    Args:
        model: 'string', url of the model to be located.
    Returns:
         None
    Throws:
        OSError
    """
    try:
        execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-locate", "-kb", model]
        path = subprocess.run(execute, capture_output=True).stdout.decode()
        return path.split("\n")[0]
    except OSError as e:
        raise OSError(e)


def locate(model, format=None, version=None):
    """ Returns the local address of the given model.
    Args:
        model: 'string',url of the model to be installed.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
         None
    Throws:
        OSError
    """
    try:
        execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-locate", "-kb", model]
        if format is not None:
            execute.append("-format")
            execute.append(format)
            if version is not None:
                execute.append("-version")
                execute.append(version)
        # return subprocess.check_output(execute).decode("utf-8")
        path = subprocess.run(execute, capture_output=True).stdout.decode()
        return path.split("\n")[0]
    except OSError as e:
        raise OSError(e)


def search(pattern, format=None, version=None):
    """ Search for all model-ids containing a given pattern.
    Args:
        pattern: 'string',pattern of the url of the models.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        None
    Throws:
        OSError
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
    """ Show the path to the folder which contains the models.
    Returns:
        Path of the installed models.
    Throws:
        OSError
    """
    try:
        execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-r-dir"]
        path = subprocess.run(execute, capture_output=True).stdout.decode()
        return path[36:-1]
    except OSError as e:
        raise OSError(e)


def setModelDirPath(dir):
    """ Change the path of the resource folder.
    Args:
        dir:'string', new model path
    Returns:
        None
    Throws:
        OSError
    """
    try:
        execute = JAR_EXECUTE + SPACE + "-r-dir" + SPACE + dir
        os.system(execute)
    except OSError as e:
        raise OSError(e)


def showVersion():
    """ Returns KBox version.
    Returns:
        KBox version.
    Throws:
        OSError
    """
    try:
        execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar","-version"]
        version = subprocess.run(execute, capture_output=True).stdout.decode()
        return version[:-1]
    except OSError as e:
        raise OSError(e)


# if __name__ == '__main__':
#     # install("http://github.org/aksw/NSpM/monument_300", "NSPM/Model", "0")
#     # print(getModelDirPath())
#     print(showVersion())

