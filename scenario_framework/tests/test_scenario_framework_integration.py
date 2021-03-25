from powersimdata import Scenario
import uuid
import pytest
import os


def test_scenario_server_container_up():
    hostname = "scenario_server"
    response = os.system("ping -c 1 " + hostname)
    assert response == 0


@pytest.mark.skip(reason="we will add reisejl container later")
def test_reise_jl_container_up():
    hostname = "reisejl"
    response = os.system("ping -c 1 " + hostname)
    assert response == 0


@pytest.fixture
def scenario():
    scenario = Scenario()

    scenario.set_grid(grid_model="usa_tamu", interconnect="Texas")
    scenario.set_name(
        "test" + "_" + str(uuid.uuid1()), "dummy" + "_" + str(uuid.uuid1())
    )
    scenario.set_time("2016-08-01 00:00:00", "2016-08-31 23:00:00", "24H")

    scenario.set_base_profile("demand", "vJan2021")
    scenario.set_base_profile("hydro", "vJan2021")
    scenario.set_base_profile("solar", "vJan2021")
    scenario.set_base_profile("wind", "vJan2021")
    return scenario


@pytest.mark.integration
@pytest.mark.ssh
def test_scenario_1712_analysis():
    scenario = Scenario("1712")
    # print scenario information
    scenario.print_scenario_info()
    # get change table
    ct = scenario.get_ct()
    # get grid
    grid = scenario.get_grid()
    # get demand profile
    demand = scenario.get_demand()
    # get hydro profile
    hydro = scenario.get_hydro()
    # get solar profile
    solar = scenario.get_solar()
    # get wind profile
    wind = scenario.get_wind()
    # get generation profile for generators
    pg = scenario.get_pg()
    # get power flow profile for AC lines
    pf_ac = scenario.get_pf()
    # get locational marginal price profile for each bus
    lmp = scenario.get_lmp()
    # get congestion (upper power flow limit) profile for AC lines
    congu = scenario.get_congu()
    # get congestion (lower power flow limit) profile for AC lines
    congl = scenario.get_congl()
    # get time averaged congestion (lower and power flow limits) for AC lines
    avg_cong = scenario.get_averaged_cong()
    # get generation profile for storage units (if present in scenario)
    pg_storage = scenario.get_storage_pg()
    # get energy state of charge of storage units (if present in scenario)
    e_storage = scenario.get_storage_e()


@pytest.mark.integration
@pytest.mark.ssh
def test_create_base_grid_texas_scenario(scenario):
    scenario.create_scenario()
    scenario.prepare_simulation_input()

    scenario.print_scenario_info()


@pytest.mark.integration
@pytest.mark.ssh
def test_create_and_upload_texas_scenario(scenario):
    scenario.change_table.scale_plant_capacity(
        "solar", zone_name={"Far West": 5, "West": 2.5}
    )
    scenario.change_table.scale_plant_capacity(
        "wind", zone_name={"South": 1.5, "North Central": 2}
    )
    scenario.change_table.scale_branch_capacity(
        zone_name={"South": 2, "North Central": 2}
    )

    new_bus_id = scenario.get_grid().bus.index.max() + 1
    scenario.change_table.add_bus([{"lat": 30, "lon": -95, "zone_id": 308}])
    scenario.change_table.add_storage_capacity(
        [{"bus_id": int(new_bus_id), "capacity": 100}]
    )
    scenario.change_table.add_plant(
        [{"type": "wind", "bus_id": new_bus_id, "Pmax": 400}]
    )
    scenario.change_table.add_branch(
        [{"from_bus_id": (new_bus_id - 1), "to_bus_id": new_bus_id, "capacity": 300}]
    )

    scenario.change_table.scale_renewable_stubs()
    scenario.create_scenario()
    scenario.prepare_simulation_input()

    scenario.print_scenario_info()
