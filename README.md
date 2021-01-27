# plug
PortabLe infrastUrcture for Grid modelling


### How to use
To run the containerized framework, the only prerequisite is to have raw profiles located the `raw/` directory, at the root of the repository, as well as a gurobi license. 

With that, you can `cd standalone` and run `docker-compose-up`. In a separate shell, attach to the powersimdata client using

```
docker-compose exec powersimdata ipython
```

and follow the workflow defined in the powersimdata [readme](https://github.com/Breakthrough-Energy/PowerSimData). 
