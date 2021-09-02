# plug
PortabLe infrastrUcture for Grid modeling

## Prerequisites
To use *plug* you'll need to have docker installed - visit their [website](https://docs.docker.com/get-docker/)
for details.

If you want to run simulations using the Gurobi solver (recommended), you'll need a
license file called `gurobi.lic` located at `plug/gurobi_license/gurobi.lic`

*NOTE*: certain license types are not supported at the moment. 


## How to use

We describe the workflow for running a standalone installation on a single
computer. To get started, run `cd standalone` in your shell, followed by
`docker-compose up` (optionally pass `-d` to run in the background). 
The docker images will be downloaded automatically 
from our [container registry](https://github.com/orgs/Breakthrough-Energy/packages).

The `client` container contains both [PowerSimData] and [PostREISE] packages, for
scenario management and analysis, respectively. The default compose file starts the
client running `bash`, which serves as an entrypoint to either an `ipython` shell:

```
docker-compose exec client ipython
```
 or a jupyter notebook:

```
docker-compose exec client jupyter lab --port=10000 --no-browser --ip=0.0.0.0 --allow-root
```

See the PowerSimData [tutorial] for details 
about how to run a simulation, or try the commands in `demo_*.py` for a simple example.

The usage within the containerized setup is almost identical to what is
presented in the PowerSimData repo, but there are some small differences. 

1) When calling `scenario.launch_simulation()`, the process is launched
via http rather than ssh, and we provide a container specific way to query the
status. This can be done using `scenario.check_progress()` which will
return some output in the following form.

```
{'errors': [],
 'output': ['Validation complete!',
  'Launching scenario with parameters:',
  "{'interval': 24, 'n_interval': 2, 'start_index': 5113, 'input_dir': '/mnt/bes/pcm/tmp/scenario_1', 'execute_dir': '/mnt/bes/pcm/tmp/scenario_1/output', 'threads': None}"],
 'scenario_id': 1,
 'status': 'running'}
```

Note that the `errors/output` fields correspond to lines of
`stderr/stdout`, respectively.

2) Once the simulation is complete, the results are extracted automatically, so
there is no need to call `scenario.extract_simulation_output()` (although
doing so will simply print a warning). The data can be accessed from the
`Analyze` state within the container, but if you have a use case that is not
yet supported, the data can be detached from docker, which we describe below.

## Extracting data
Currently, the simplest way to access simulation output is by copying the
results from the container. To copy the full volume as-is, use the following:

```
docker cp client:/mnt/bes/pcm DEST_FOLDER
```

Optionally, to snapshot the results to a tar archive, run

```
docker cp client:/mnt/bes/pcm - > FILENAME.tar
```

## Local development
If you want to build any of the docker images locally you should use the following 
directory structure so relative paths will work.

```bash
    .
    ├── plug
    └── REISE.jl
```

Then, to build the images when starting, use the override feature described [here][override],
for example
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

## Client/server architecture

The contents of the `scenario_framework` folder are provided to mirror the client server
architecture used internally and enable reproducible testing in that
environment. Note: this is not currently recommended for general research
purposes, however developers who wish to run integration tests without access
to the server may find this useful.

The basic operation is similar to standalone mode described earlier. First `cd`
to the `scenario_framework` directory, which has the compose file for this
environment. The integration tests can be run using the following:

```
docker-compose up -d
docker exec scenario_client bash -c 'pytest -m "not db"'
```

In addition to the test suite from PowerSimData, this will run the tests
provided here, which demonstrate typical user workflows. 

[PowerSimData]: https://github.com/Breakthrough-Energy/PowerSimData
[PostREISE]: https://github.com/Breakthrough-Energy/PostREISE
[tutorial]: https://breakthrough-energy.github.io/docs/powersimdata/index.html
[override]: https://docs.docker.com/compose/extends/
