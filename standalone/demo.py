from uuid import uuid4

from powersimdata.scenario.scenario import Scenario

scenario = Scenario("")
print(scenario.state.name)

scenario.state.set_builder(["Texas"])

scenario.state.builder.set_name("test", "dummy_" + str(uuid4()))
scenario.state.builder.set_time("2016-08-01 00:00:00", "2016-08-01 03:00:00", "1H")

scenario.state.builder.set_base_profile("demand", "ercot")
scenario.state.builder.set_base_profile("hydro", "v2")
scenario.state.builder.set_base_profile("solar", "v4.1")
scenario.state.builder.set_base_profile("wind", "v5.1")


scenario.state.builder.change_table.add_bus([{"lat": 30, "lon": -95, "zone_id": 308}])


grid = scenario.state.get_grid()
ct = scenario.state.get_ct()

scenario.state.print_scenario_info()
scenario.state.create_scenario()

scenario.state.prepare_simulation_input()

resp = scenario.state.launch_simulation(solver="glpk")
scenario.state.check_progress()
