## Tutorial

This guide is to facilitate the use of the notebooks for training purposes.
In them, there is a quick tour of the framework, going through the following stages:

1. Analyzing results from an existing scenario
2. Using those results to build a new scenario
3. More in depth analysis of the subsequent results
4. Visualize the results using PostREISE

### Installation
First clone the repository as follow
```
git clone https://github.com/Breakthrough-Energy/plug.git
```

Currently, the notebooks are located in the `jen/training` branch, so switch to that
using (ensure you are in the `plug` directory first)
```
git checkout origin/jen/training
```

To use *plug* you'll need to have docker installed - visit their [website](https://docs.docker.com/get-docker/)
for details.

### Dataset

One benefit of using *plug* is that arbitrary sets of scenario data can be prepared,
and attached to the container(s), allowing one to "swap out" one data set for another.

One such example is available [here][training_data] (size is 5.2G)

**NOTE** - data for the training session on Wed, 4/28 is available [here][miso_training] (size is 6.4G)

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

If you need to switch to a new dataset, this can be done by:
- stopping the containers (`Ctrl-c` in the terminal running docker-compose)
- remove the containers - `docker container prune`
- rename the current training folder
- extract the new dataset as above (destination folder should be called `training` regardless of the zip file name)
- restart the containers as described below.

### Running the code

Navigate to the `standalone/` folder. To make ensure your images are up to date, first run the following
command (or equivalent per image, see [postreise](https://github.com/orgs/Breakthrough-Energy/packages/container/package/postreise) example)

```
docker-compose -f training.yml pull
```
Then to run the containers

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
[miso_training]: https://bescienceswebsite.blob.core.windows.net/training/miso.zip
