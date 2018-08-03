import os
import pandas as pd
import pyomo.environ
import shutil
import urbs
from pyomo.opt.base import SolverFactory


if __name__ == '__main__':
    input_files = urbs.read_intertemporal('Input')
    result_name = 'Campus'
    result_dir = urbs.prepare_result_directory(result_name) # name + time stamp

    # copy input file to result directory
    # shutil.copyfile(input_file, os.path.join(result_dir, input_file))
    # copy runme.py to result directory
    # shutil.copyfile(__file__, os.path.join(result_dir, __file__))

    # Choose Solver (cplex, glpk, gurobi, ...)
    Solver = 'gurobi'

    # simulation timesteps
    (offset, length) = (1000, 168)  # time step selection
    timesteps = range(offset, offset+length+1)
    dt=1

    # plotting commodities/sites
    plot_tuples = [
        (2015, 'Campus', 'Elec'),
        (2015, 'Campus', 'Heat'),
        (2015, 'Campus', 'Cold'),
        (2015, 'Campus', 'Heat low'),
        (2020, 'Campus', 'Elec'),
        (2020, 'Campus', 'Heat'),
        (2020, 'Campus', 'Cold'),
        (2020, 'Campus', 'Heat low'),
        (2025, 'Campus', 'Elec'),
        (2025, 'Campus', 'Heat'),
        (2025, 'Campus', 'Cold'),
        (2025, 'Campus', 'Heat low'),
        (2030, 'Campus', 'Elec'),
        (2030, 'Campus', 'Heat'),
        (2030, 'Campus', 'Cold'),
        (2030, 'Campus', 'Heat low'),
        (2035, 'Campus', 'Elec'),
        (2035, 'Campus', 'Heat'),
        (2035, 'Campus', 'Cold'),
        (2035, 'Campus', 'Heat low'),
        (2040, 'Campus', 'Elec'),
        (2040, 'Campus', 'Heat'),
        (2040, 'Campus', 'Cold'),
        (2040, 'Campus', 'Heat low')
        ]

    # optional: define names for sites in plot_tuples
    plot_sites_name = {}

    # detailed reporting commodity/sites
    report_tuples = [
        (2015, 'Campus', 'Elec'),
        (2015, 'Campus', 'Heat'),
        (2015, 'Campus', 'Cold'),
        (2015, 'Campus', 'Heat low'),
        (2015, 'Campus', 'CO2'),
        (2020, 'Campus', 'Elec'),
        (2020, 'Campus', 'Heat'),
        (2020, 'Campus', 'Cold'),
        (2020, 'Campus', 'CO2'),
        (2020, 'Campus', 'Heat low'),
        (2025, 'Campus', 'Elec'),
        (2025, 'Campus', 'Heat'),
        (2025, 'Campus', 'Cold'),
        (2025, 'Campus', 'Heat low'),
        (2025, 'Campus', 'CO2'),
        (2030, 'Campus', 'Elec'),
        (2030, 'Campus', 'Heat'),
        (2030, 'Campus', 'Cold'),
        (2030, 'Campus', 'Heat low'),
        (2030, 'Campus', 'CO2'),
        (2035, 'Campus', 'Elec'),
        (2035, 'Campus', 'Heat'),
        (2035, 'Campus', 'Cold'),
        (2035, 'Campus', 'Heat low'),
        (2035, 'Campus', 'CO2'),
        (2040, 'Campus', 'Elec'),
        (2040, 'Campus', 'Heat'),
        (2040, 'Campus', 'Cold'),
        (2040, 'Campus', 'Heat low'),
        (2040, 'Campus', 'CO2'),
        ]

    # optional: define names for sites in report_tuples
    report_sites_name = {}

    # plotting timesteps
    plot_periods = {
        'win': range(1000, 1000+24*7),
        # 'spr': range(3000, 3000+24*7),
        # 'sum': range(5000, 5000+24*7),
        # 'aut': range(7000, 7000+24*7)
    }

    # add or change plot colors
    my_colors = {
        'South': (230, 200, 200),
        'Mid': (200, 230, 200),
        'North': (200, 200, 230)}
    for country, color in my_colors.items():
        urbs.COLORS[country] = color

    # select scenarios to be run
    scenarios = [
                 urbs.scenario_base,
                 # urbs.sc_CO2limit(40000),
                 # urbs.sc_1proprop('Campus', 'PV S 30°', 'inv-cost', 600000)
    ]

    for scenario in scenarios:
        prob = urbs.run_scenario(input_files, Solver, timesteps, scenario,
                            result_dir, dt,
                            plot_tuples=plot_tuples,
                            plot_sites_name=plot_sites_name,
                            plot_periods=plot_periods,
                            report_tuples=report_tuples,
                            report_sites_name=report_sites_name)
