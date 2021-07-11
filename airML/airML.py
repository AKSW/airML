import os
import subprocess
import requests

import click

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
JAR_EXECUTE = "java -jar " + DIR_PATH + "/kbox-v0.0.2-beta.jar"  # kbox-v0.0.2-beta.jar
SPACE = " "

PUSH_COMMAND = 'push'

COMMAND_LIST = [PUSH_COMMAND]


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('commands', nargs=-1)
def execute_kbox_command(commands):
    if not __is_push(commands):
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
    else:
        file_path = commands[1]
        print(file_path)
        url = 'https://store9.gofile.io/uploadFile'
        files = {'file': open(file_path, 'rb')}
        r = requests.post(url, files=files)
        print(r.text)


def execute(commands):
    commands = tuple(commands.split())
    execute_kbox_command(commands)


def __is_push(command):
    if command[0] == PUSH_COMMAND:
        return True
    return False
