import pandas as pd
import pickle

from powersimdata import Grid
from powersimdata.design.investment.investment_costs import (
    _calculate_ac_inv_costs,
    _calculate_dc_inv_costs,
    _calculate_gen_inv_costs,
)


def filter_branch(df):
    cols = ["from_bus_id", "to_bus_id", "rateA"]
    return df.loc[:, cols]


def _calc_ac(grid):
    ac_raw = _calculate_ac_inv_costs(grid, sum_results=False)
    return _calc_ac_2(ac_raw)


def _calc_ac_2(ac_raw):
    branch_cost = pd.concat(ac_raw.values())
    branch_cost /= grid.branch.rateA
    branch = filter_branch(grid.branch)
    branch["cost"] = branch_cost
    return branch


def _calc_dc(grid):
    return _calculate_dc_inv_costs(grid, sum_results=False)


def _calc_gen(grid):
    return _calculate_gen_inv_costs(grid, 2020, "Moderate", sum_results=False)


grid = Grid("USA")

# NOTE: tested ac and gen for texas grid vs scenario with texas and got the same results
# need to test something with dcline, and maybe do the same as above for other
# interconnects

# TODO: add other columns to outputs, normalize, etc

ac3 = _calc_ac(grid)
dc3 = _calc_dc(grid)
gen3 = _calc_gen(grid)

with open("/plug/ac_costs.pkl", "wb") as f:
    pickle.dump(ac3, f)

with open("/plug/dc_costs.pkl", "wb") as f:
    pickle.dump(dc3, f)

with open("/plug/gen_costs.pkl", "wb") as f:
    pickle.dump(gen3, f)


def filter_plant(df):
    cols = ["bus_id", "type", "Pmax"]
    return df.loc[:, cols]


def add_cost(plant_df, cost_df):
    # plant_df.sort_index()["inv_cost"] = cost_df.sort_index()
    return pd.concat([plant_df, cost_df], axis=1)
