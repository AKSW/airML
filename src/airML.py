import subprocess
import json
import os

DEFAULT_KNS = ""
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
JAR_EXECUTE = "java -jar " + DIR_PATH + "/kbox-v0.0.2-beta.jar"  # kbox-v0.0.2-beta.jar
SPACE = " "
JSON_OUTPUT = " -o json"


def list(kns=False):
    """ List all available models(kns=False) or list all KNS services(kns=True).
    Args:
      kns:'boolean',defines whether to list only the KNS services or not
    Returns:
        json
    """

    if kns:
        execute = JAR_EXECUTE + SPACE + "-list" + SPACE + "-kns"
    else:
        execute = JAR_EXECUTE + SPACE + "-list"
    execute += JSON_OUTPUT
    return __execute_command(execute)


def install(modelID, format=None, version=None):
    """ Install the a model by given modelID
    Args:
        modelID: 'string', url of the model hosted in a public repository.
        format:  'string', format of the model.
        version: 'string' specific version to be installed of the the model.
    Returns:
        json
    Example:
        install("http://github.org/aksw/NSpM/monument_300","NSPM/Model","0")
    """

    execute = JAR_EXECUTE + SPACE + "-install" + SPACE + "-kb" + SPACE + modelID
    if format is not None:
        execute += (SPACE + "-format" + SPACE + format)
    elif format is not None:
        execute += (SPACE + "-format" + SPACE + format)
        if version is not None:
            execute += (SPACE + "-version" + SPACE + version)
    execute += (SPACE + "-kns" + SPACE + DEFAULT_KNS + JSON_OUTPUT)
    return __execute_command(execute)


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
    if kns is not None:
        execute += (SPACE + "-kns" + SPACE + kns)
        if format is not None:
            execute += (SPACE + "-format" + SPACE + format)
    elif format is not None:
        execute += (SPACE + "-format" + SPACE + format)
        if version is not None:
            execute += (SPACE + "-version" + SPACE + version)
    execute += JSON_OUTPUT
    return __execute_command(execute)


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
    execute = JAR_EXECUTE + SPACE + "-remove" + SPACE + "-kns" + SPACE + kns + JSON_OUTPUT
    return __execute_command(execute)


def getInfo(model, format=None, version=None):
    """ Gives the information about a specific model.
    Args:
        model: url of the model.
        format: format of the model.
        version: version of the model.
    Return:
        None
    Throws:
        OSError
    """
    execute = JAR_EXECUTE + SPACE + "-info" + SPACE + model
    if format is not None:
        execute += (SPACE + "-format" + SPACE + format)
        if version is not None:
            execute += (SPACE + "-version" + SPACE + version)
    execute += JSON_OUTPUT
    return __execute_command(execute)


def locate(modelID, format=None, version=None):
    """ Returns the local address of the given model.
    Args:
        modelID: 'string',url of the model to be located.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
         None
    Throws:
        OSError
    """
    # execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-locate", "-kb", modelID]
    execute = JAR_EXECUTE + SPACE + "-locate" + SPACE + "-kb" + SPACE + modelID
    if format is not None:
        execute += SPACE + "-format" + SPACE + format
        # execute.append("-format")
        # execute.append(format)
        if version is not None:
            execute += SPACE + "-version" + SPACE + version
            # execute.append("-version")
            # execute.append(version)
    execute += JSON_OUTPUT
    return __execute_command(execute)


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
    execute = JAR_EXECUTE + SPACE + "-search" + SPACE + pattern
    if format is not None:
        execute += (SPACE + "-format" + SPACE + format)
        if version is not None:
            execute += (SPACE + "-version" + SPACE + version)
    execute += JSON_OUTPUT
    return __execute_command(execute)


def getModelDirPath():
    """ Show the path to the folder which contains the models.
    Returns:
        Path of the installed models.
    Throws:
        OSError
    """
    # execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-r-dir"]
    execute = JAR_EXECUTE + SPACE + "-r-dir" + JSON_OUTPUT
    # path = subprocess.run(execute, capture_output=True).stdout.decode()
    return __execute_command(execute)


def setModelDirPath(dir):
    """ Change the path of the resource folder.
    Args:
        dir:'string', new model path
    Returns:
        None
    Throws:
        OSError
    """
    execute = JAR_EXECUTE + SPACE + "-r-dir" + SPACE + dir + JSON_OUTPUT
    return __execute_command(execute)


def showVersion():
    """ Returns KBox version.
    Returns:
        KBox version.
    Throws:
        OSError
    """
    try:
        # execute = ["java", "-jar", "kbox-v0.0.2-alpha.jar", "-version"]
        execute = JAR_EXECUTE + SPACE + "-version" + JSON_OUTPUT
        # version = subprocess.run(execute, capture_output=True).stdout.decode()
        return __execute_command(execute)
    except OSError as e:
        raise OSError(e)


def __execute_command(execute):
    try:
        process = subprocess.Popen(execute.split(), stdout=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        json_output = json.loads(output)
        return json_output
    except OSError as e:
        print(e)

# if __name__ == '__main__':
#     # install("http://github.org/aksw/NSpM/monument_300", "NSPM/Model", "0")
#      #"/home/oshara/.kbox"
#
#     # print(showVersion())
#
#     # print(locate("http://github.org/aksw/NSpM/monument_300", "NSPM/Model", "0"))
#     # getInfo("http://github.org/aksw/NSpM/monument_300", "NSPM/Model", "0")
#     # print(search("NSPM/Model",version="0"))
#
#     # setModelDirPath("/home/test/kbox/test/models")
#     # print(getModelDirPath())
