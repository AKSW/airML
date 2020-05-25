# airML

This package is created to distribute KBox, which allow users to share and dereference ML models.

* Download the library [here] (https://pypi.org/project/airML/)

* Install using pip
```
pip install airML
```

### Use it in your python application.

##### list(kns=False)
    Description:List all available models(kns=False) or list all KNS services(kns=True).
    Args:
      kns:'boolean',defines whether to list only the KNS services or not
    Returns:
        None
    Throws:
        OSError
##### install(modelID, format=None, version=None)
    Description:Install the a model by given modelID
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
 
##### install(modelID, format=None, version=None, kns=None)
    Description:Install a given model base using the available KNS services to resolve it.
    Args:
        modelID:'string',url of the model to be installed.
        format: 'string',format of the model.
        version:'string',version of the model.
        kns:'string', url of the kns service.
    Returns:
        None
    Throws:
        OSError

##### removeKNS(kns)
    Description:Remove a given KNS service.
    Args:
        kns:'string', url of the kns service.
    Returns:
        None
    Throws:
        OSError

##### getInfo(model, format=None, version=None)
    Description:Gives the information about a specific model.
    Args:
        model: url of the model to be installed.
        format: format of the model.
        version: version of the model.
    Return:
        None
    Throws:
        OSError
   
##### locate(modelID, format=None, version=None)
    Description:Find the local address of the given model.
    Args:
        modelID: 'string', url of the model to be located.
        format: 'string', format of the model.
        version: 'string', version of the model
    Returns:
         None
    Throws:
        OSError

##### search(pattern, format=None, version=None)
    Description:Search for all model-ids containing a given pattern.
    Args:
        pattern: 'string',pattern of the url of the models.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        None
    Throws:
        OSError
    
##### getModelDirPath()
    Description:Show the path to the folder which contains the models.
    Returns:
        Path of the installed models.
    Throws:
        OSError

##### setModelDirPath(dir)
    Description:Change the path of the resource folder.
    Args:
        dir:'string', new model path
    Returns:
        None
    Throws:
        OSError
 
##### showVersion()
    Description:Returns KBox version.
    Returns:
        KBox version.
    Throws:
        OSError
 
#### Running Tests
* By executing the below command you can run the tests.
    ```
    python -m unittest test_airML.py
    ```
#### Source URLs
* See the source for this project [here] (https://github.com/AKSW/airML)
* Find the KBox source code [here] (https://github.com/AKSW/KBox)
