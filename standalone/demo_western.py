from uuid import uuid4

from powersimdata import Scenario

scenario = Scenario()
print(scenario.state.name)

scenario.set_grid(interconnect="Western")

scenario.set_name("test", "run_readme_to_test_grid_model_" + str(uuid4()))
scenario.set_time("2016-08-01 00:00:00", "2016-08-02 23:00:00", "24H")

scenario.set_base_profile("demand", "vJan2021")
scenario.set_base_profile("hydro", "vJan2021")
scenario.set_base_profile("solar", "vJan2021")
scenario.set_base_profile("wind", "vJan2021")

# scale capacity of solar plants in WA and AZ by 5 and 2.5, respectively
scenario.change_table.scale_plant_capacity(
    "solar", zone_name={"Washington": 5, "Arizona": 2.5}
)
# scale capacity of wind farms in OR and MT by 1.5 and 2, respectively
scenario.change_table.scale_plant_capacity(
    "wind", zone_name={"Oregon": 1.5, "Montana Western": 2}
)
# scale capacity of branches in NV and WY by 2
scenario.change_table.scale_branch_capacity(zone_name={"Nevada": 2, "Wyoming": 2})

# add AC lines in NM and CO
scenario.change_table.add_branch(
    [
        {"capacity": 200, "from_bus_id": 2053002, "to_bus_id": 2053303},
        {"capacity": 150, "from_bus_id": 2060002, "to_bus_id": 2060046},
    ]
)

# add DC line between CO and CA (Bay Area)
scenario.change_table.add_dcline(
    [{"capacity": 2000, "from_bus_id": 2060771, "to_bus_id": 2021598}]
)

# add a solar plant in NV, a coal plant in ID and a natural gas plant in OR
scenario.change_table.add_plant(
    [
        {"type": "solar", "bus_id": 2030454, "Pmax": 75},
        {
            "type": "coal",
            "bus_id": 2074334,
            "Pmin": 25,
            "Pmax": 750,
            "c0": 1800,
            "c1": 30,
            "c2": 0.0025,
        },
        {
            "type": "ng",
            "bus_id": 2090018,
            "Pmax": 75,
            "c0": 900,
            "c1": 30,
            "c2": 0.0015,
        },
    ]
)

# add a new bus, and a new one-way DC line connected to this bus
scenario.change_table.add_bus([{"lat": 48, "lon": -125, "zone_id": 201, "baseKV": 138}])
scenario.change_table.add_dcline(
    [{"from_bus_id": 2090023, "to_bus_id": 2090024, "Pmin": 0, "Pmax": 200}]
)


grid = scenario.get_grid()
ct = scenario.get_ct()

scenario.print_scenario_info()
scenario.create_scenario()

scenario.prepare_simulation_input()

resp = scenario.launch_simulation()
scenario.check_progress()
