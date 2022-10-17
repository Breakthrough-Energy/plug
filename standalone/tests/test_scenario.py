import time
from uuid import uuid4

from powersimdata import Scenario


def create_default():
    scenario = Scenario()
    scenario.set_grid(interconnect="Texas")
    scenario.set_name("test", "comp_" + str(uuid4()))
    scenario.set_time("2016-01-01 00:00:00", "2016-01-01 03:00:00", "2H")

    scenario.set_base_profile("demand", "vJan2021")
    scenario.set_base_profile("hydro", "vJan2021")
    scenario.set_base_profile("solar", "vJan2021")
    scenario.set_base_profile("wind", "vJan2021")
    scenario.print_scenario_info()
    return scenario


def launch(scenario):
    scenario.create_scenario()
    scenario.prepare_simulation_input()
    scenario.launch_simulation(solver="glpk")


def wait(scenario):
    while True:
        time.sleep(10)
        prog = scenario.check_progress()
        if prog["status"] == "extracted":
            break
        if prog["status"] == "failed":
            print(prog["output"])
            raise Exception("scenario failed")


def test_lifecycle():
    scenario = create_default()
    launch(scenario)
    wait(scenario)


def test_storage():
    scenario = create_default()
    scenario.change_table.add_storage_capacity(
        [
            {"bus_id": 3002011, "capacity": 751, "duration": 1},
            {"bus_id": 3003048, "capacity": 750, "duration": 1},
            {"bus_id": 3005055, "capacity": 750, "duration": 1},
            {"bus_id": 3007366, "capacity": 750, "duration": 1},
        ]
    )
    launch(scenario)
    wait(scenario)
