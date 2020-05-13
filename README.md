# airML

This package is created to distribute KBox, which allow users to share and dereference ML models.

* Download the library [here] (https://pypi.org/project/airML/)

* Install using pip
```
pip install airML
```

### Use it in your python application.

##### * list(kns=False)
    List all available models(kns=False) or list all KNS services(kns=True).
    :param kns: Define whether to list only the KNS services or not  :type boolean
    :return None
    :throws OSError

##### * install(modelUrl)
    Install a given model by given URL.
    :param modelUrl: the url of the model to be installed :type string
    :return None
    :throws OSError
    

##### * installKNS(kns)
    Install a given KNS service.
    :param kns: url of the kns service :type string
    :return None
    :throws OSError

##### * iinstall(model, format=None, version=None, index=None, kns=None)
     Install a given model base using the available KNS services to resolve it.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :param index: index of the model :type string
    :param kns: url of the kns service :type string
    :return None
    :throws OSError

##### * removeKNS(kns)
     Remove a given KNS service.
    :param kns: url of the kns service :type string
    :return None
    :throws OSError

##### * getInfo(model, format=None, version=None)
     Gives the information about a specific model.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError

##### * locate(model)
     returns the local address of the given model.
    :param model: url of the model to be installed :type string
    :return None
    :throws OSError

##### * locate(model, format=None, version=None)
    returns the local address of the given KB.
    :param model: url of the model to be installed :type string
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError

##### * search(pattern, format=None, version=None)
     Search for all model-ids containing a given pattern.
    :param pattern: pattern of the url of the models
    :param format: format of the model :type string
    :param version: version of the model :type string
    :return None
    :throws OSError

##### * getModelDirPath()
     Show the path to the folder which contains the models.
    :return None
    :throws OSError

##### * setModelDirPath(dir)
     Change the path of the resource folder.
    :param dir: new model path
    :return None
    :throws OSError

##### * showVersion()
     display KBox version.
    :return None
    :throws OSError

#### Source URLs
* See the source for this project [here] (https://github.com/AKSW/airML)
* Find the KBox source cord [here] (https://github.com/AKSW/KBox)
