# airML
Distributed Deployment of ML models at scale

This package is created to distribute KBox, which allow users to share and dereference ML models.

* Download the library [here](https://test.pypi.org/project/airML/)

* Install using pip
```
pip install airML
```

### Use it in from your terminal
Once you install the airML package, you can directly execute the commands from the terminal. You don't need to open 
up a python environment to use the airML package.

Open a terminal and execute KBox commands in python with airML package as below,

````
airML list -o json
````
**Note: Here the `-o json` is an optional parameter. If you want to get the output as a json message, you should use this. 
Otherwise, use the command without `-o json`.

````
{
    "status_code": 200,
    "message": "visited all KNs.",
    "results": [
        {
            "name": "http://purl.org/pcp-on-web/dbpedia",
            "format": "kibe",
            "version": "c9a618a875c5d46add88de4f00b538962f9359ad"
        },
        {
            "name": "http://purl.org/pcp-on-web/ontology",
            "format": "kibe",
            "version": "c9a618a875c5d46add88de4f00b538962f9359ad"
        },
        {
            "name": "http://purl.org/pcp-on-web/dataset",
            "format": "kibe",
            "version": "dd240892384222f91255b0a94fd772c5d540f38b"
        }
    ]
}

````

Like the above command, you can use all other KBox commands with airML package. You can refer to the document 
[here](https://github.com/AKSW/KBox#how-can-i-execute-kbox-in-command-line) to get a good understanding of other KBox commands as well. 

### Use it in your python application.

##### execute(command)
    Description: Execute the provided command in the KBox.jar
    Args:
      command: 'string', KBox command which should be exectue in KBox.
    Returns:
        string

If you want to use the airML inside your python application, you can follow these instructions,
1. Import the airML package (`from airML import airML`).
2. Execute any KBox command with execute() function as follows.
   
   ```
   airML.execute('KBox_Command')
   ```

**Note: `execute()` method will return a string output which contains the result of the executed command.

Other than the execute command you can use following methods directly,

##### list(kns=False)
    Description: List all available models(kns=False) or list all KNS services(kns=True).
    Args:
      kns:'boolean',defines whether to list only the KNS services or not
    Returns:
            Results from the KBox as JSON String


##### install(modelID, format=None, version=None):
    Description: Install the a model by given modelID
     Args:
         modelID: 'string', url of the model hosted in a public repository.
         format:  'string', format of the model.
         version: 'string' specific version to be installed of the the model.
     Returns:
         Results from the kbox as JSON String
     Example:
         install("http://nspm.org/art","NSPM","0")

##### getInfo(model):
    Description: Gives the information about a specific model.
    Args:
        model: url of the model.
    Return:
        Results from the kbox as JSON String

##### locate(modelID, format, version=None):
    Description: Returns the local address of the given model.
    Args:
        modelID: 'string',url of the model to be located.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        Results from the kbox as JSON String

##### search(pattern, format, version=None):
    Description: Search for all model-ids containing a given pattern.
    Args:
        pattern: 'string',pattern of the url of the models.
        format: 'string',format of the model.
        version: 'string',version of the model.
    Returns:
        Search Result from the KBox as a JSON String
    
### Source URLs
* See the source for this project [here](https://github.com/AKSW/airML)
* Find the KBox source code [here](https://github.com/AKSW/KBox)
