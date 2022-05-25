## Tutorial

This guide is to facilitate the use of the notebooks for training purposes.
In them, there is a quick tour of the framework, going through the following stages:

1. Analyzing results from an existing scenario
2. Using those results to build a new scenario
3. More in depth analysis of the subsequent results
4. Visualize the results using PostREISE

### Dataset

Data for the notebooks is provided in a zip file, available [here][training_data].
It is fairly large (5.2G) so allow some time for this.

To use this data within the containerized environment, make sure it is located within
the repository, and extract the files like so:

```bash
    .
    ├── plug
        ├── training.zip
        └── training/
```

On unix systems, `unzip training.zip` should work. For windows powershell:

```
Expand-Archive -Path training.zip -DestinationPath .
```

### Running the code

Navigate to the `standalone/` folder and run the following.

```
docker-compose -f training.yml up
```

This starts up two containers:
* client - used for interaction via a jupyter notebook
* reisejl - hosts the engine used for running simulations

You should see some output containing a url path to access the notebook
which will look something like 

```
 http://127.0.0.1:10000/lab?token=d2426033dfcfff045fb7e5ec8705f1e19b40dc2a8491cec1
```

Paste that into your browser and you will have access to all the notebooks, data,
and python environment for interacting with the framework.


[training_data]: https://bescienceswebsite.blob.core.windows.net/training/training.zip
