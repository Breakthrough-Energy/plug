# plug
PortabLe infrastUrcture for Grid modelling


### How to use
To run the containerized framework, the only prerequisite is to have a gurobi
license at the root of the repository, called `gurobi.lic`.

We describe the workflow for running a standalone installation on a single
computer. To get started, run `cd standalone` in your shell, followed by
`docker-compose up`. In a separate shell, attach to the powersimdata client using

```
docker-compose exec powersimdata ipython
```

See the powersimdata [readme](https://github.com/Breakthrough-Energy/PowerSimData) for details 
about how to run a simulation, or try the commands in `demo.py` for a simple example.

### Extracting data
Currently, the simplest way to access simulation output is by copying the
results from the container. To copy the full volume as-is, use the following:

```
docker cp powersimdata:/mnt/bes/pcm DEST_FOLDER
```

Optionally, to snapshot the results to a tar archive, run

```
docker cp powersimdata:/mnt/bes/pcm - > FILENAME.tar
```

### Client/server architecture

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

In addition to the test suite from powersimdata, this will run the tests
provided here, which demonstrate typical user workflows. 
