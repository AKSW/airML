# airML

This package is created to distribute KBox, which allow users to share and dereference ML models.

* Download the library [here] (https://pypi.org/project/airML/)

* Install using pip
```
pip install airML
```

### Use it in your python application.

##### createIndex(dir)
* This method will create an index with the files in a given directory.
dir - path of the dirctory.

##### serialize(dir)
* This method will serialize the content of a directory to be served in a KNS system.
dir - path of the dirctory.

##### sparql(query)

##### server(port="8080",subDomain="kbox",kb)
* This will start an SPARQL enpoint in the given subDomain containing the given KB.
* port - default is 8080.
* subDomain - default is kbox.

##### showList(kns=False)
* If kns is not specified, this method will list all available knowledge bases.
* If you specify kns as 'True', the method will list all availables KNS services.

##### installByUrl(url)
* Install a given resource.
* url - resource url

##### installKNS(kns)
* Install a given KNS service.
* kns - kns url

##### installKB(kb,format=None,version=None,index=None,kns=None)
* Install a given knowledge base using the available KNS services to resolve it.
* kb - knowlede base url
* format - specify kb format
* version - specify kb version
* index - specify the index to be install for the given kb url
* kns - specify a kns service

##### removeKNS(kns)
* Remove a given KNS service.
* kns - kns service url

##### getInfo(url,format=None,version=None)
* Gives the information about a specific KB
* url - kb url
* format - specify kb format
* version - specify kb version

##### locateResource(url)
* Returns the local address of the given resource.
* url - url of the resource to locate

##### locateKB(url,format=None,version=None)
* returns the local address of the given KB.
* url - kb url
* format - specify kb format
* version - specify kb version

##### search(pattern)
* Search for all kb-URL containing a given pattern.
* pattern - patter of kb

##### getResourceDirPath()
* Show the path to the resource folder.

##### changeResourceDirPath(dir)
* Change the path of the resource folder.
* dir - pathe to relocate the resource folder

##### showVersion()
* display KBox version.


#### Source URLs
* See the source for this project [here] (https://github.com/AKSW/airML)
* Find the KBox source cord [here] (https://github.com/AKSW/KBox)
