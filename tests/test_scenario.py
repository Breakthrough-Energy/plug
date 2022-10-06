import time
from uuid import uuid4

from powersimdata import Scenario


def test_lifecycle():
    scenario = Scenario()
    scenario.set_grid(interconnect="Texas")
    scenario.set_name("test", "comp_" + str(uuid4()))
    scenario.set_time("2016-01-01 00:00:00", "2016-01-01 03:00:00", "1H")

    scenario.set_base_profile("demand", "vJan2021")
    scenario.set_base_profile("hydro", "vJan2021")
    scenario.set_base_profile("solar", "vJan2021")
    scenario.set_base_profile("wind", "vJan2021")

    scenario.print_scenario_info()
    scenario.create_scenario()

    scenario.prepare_simulation_input()

    scenario.launch_simulation(solver="glpk")

    while True:
        time.sleep(10)
        prog = scenario.check_progress()
        if prog["status"] == "extracted":
            break
        if prog["status"] == "failed":
            print(prog["output"])
            raise Exception("scenario failed")
