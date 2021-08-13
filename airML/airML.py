import os
import subprocess
import requests

import click

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
JAR_EXECUTE = "java -jar " + DIR_PATH + "/kbox-v0.0.2-beta.jar"  # kbox-v0.0.2-beta.jar
SPACE = " "
JSON_OUTPUT = " -o json"

PUSH_COMMAND = 'push'

COMMAND_LIST = [PUSH_COMMAND]


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('commands', nargs=-1)
def execute_kbox_command(commands):
    args = SPACE
    for item in commands:
        args += item + SPACE
    execute_commands = JAR_EXECUTE + args
    try:
        process = subprocess.Popen(execute_commands.split(), stdout=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        click.echo(output)
    except OSError as e:
        click.echo(e)


def execute(commands):
    commands = tuple(commands.split())
    args = SPACE
    for item in commands:
        args += item + SPACE
    execute_commands = JAR_EXECUTE + args
    try:
        process = subprocess.Popen(execute_commands.split(), stdout=subprocess.PIPE)
        output, err = process.communicate()
        output = output.decode("utf-8")
        return output
    except OSError as e:
        print(e)


def list(kns=False):
    """ List all available models(kns=False) or list all KNS services(kns=True).
        Args:
          kns:'boolean',defines whether to list only the KNS services or not
        Returns:
            Results from the KBox as JSON String
    """
    if kns:
        return execute('list kns' + JSON_OUTPUT)
    else:
        return execute('list' + JSON_OUTPUT)


def install(modelID, format=None, version=None):
    """ Install the a model by given modelID
        Args:
            modelID: 'string', url of the model hosted in a public repository.
            format:  'string', format of the model.
            version: 'string' specific version to be installed of the the model.
        Returns:
            Results from the kbox as JSON String
        Example:
            install("http://nspm.org/art","NSPM","0")
        """
    command = 'install ' + modelID
    if format is not None:
        command += SPACE + '-format' + SPACE + format
    if version is not None:
        command += SPACE + '-version' + SPACE + version
    return execute(command + JSON_OUTPUT)


def getInfo(model):
    """ Gives the information about a specific model.
    Args:
        model: url of the model.
    Return:
        Results from the kbox as JSON String
    """
    command = "info" + SPACE + model
    return execute(command + JSON_OUTPUT)


def locate(modelID, format, version=None):
    """ Returns the local address of the given model.
    Args:
        modelID: 'string',url of the model to be located.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        Results from the kbox as JSON String
    """
    command = 'locate' + SPACE + modelID + SPACE + '-format' + SPACE + format
    if version is not None:
        command += SPACE + '-version' + version
    return execute(command + JSON_OUTPUT)


def search(pattern, format=None, version=None):
    """ Search for all model-ids containing a given pattern.
    Args:
        pattern: 'string',pattern of the url of the models.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        Search Result from the KBox as a JSON String
    """

    command = 'search' + SPACE + pattern
    if format is not None:
        command += SPACE + "-format" + SPACE + format
        if version is not None:
            command += SPACE + "-version" + SPACE + version
    return execute(command + JSON_OUTPUT)

