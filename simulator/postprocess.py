import numpy as np

def compute_post_results(result, nodes, Cp, beta):
    sink_results = {}
    total_mass_flow = 0

    for nid, data in result.items():
        demand = nodes[nid]['demand']
        delta_T = data['Ts'] - data['Tr']
        mass_flow = demand / (Cp * delta_T)
        cost = Cp * mass_flow * delta_T
        pressure_penalty = beta * ((data['Ps'] - data['Pr']) ** 2)
        total_mass_flow += mass_flow

        sink_results[nid] = {
            'mass_flow': mass_flow,
            'heat_supplied': mass_flow * Cp * delta_T,
            'demand_met': demand,
            'cost': cost,
            'pressure_penalty': pressure_penalty,
            'objective': cost + pressure_penalty,
            'entry_pressure': data['Ps'],
            'exit_pressure': data['Pr'],
            'Ts': data['Ts'],
            'Tr': data['Tr']
        }

    # --- heater output ---
    heater_output = {
        'mass_flow_out': total_mass_flow,
        'Ts': np.max([r['Ts'] for r in result.values()]),  # take max supply temp needed
        'Tr': np.mean([r['Tr'] for r in result.values()]),
        'Ps': np.max([r['Ps'] for r in result.values()]),
        'Pr': np.min([r['Pr'] for r in result.values()])
    }

    return sink_results, heater_output

def compute_pipe_flows(sink_results):
    total_mass_flow = sum([v['mass_flow'] for v in sink_results.values()])
    pipes = {
    ('H', 'J1'): total_mass_flow,
    ('J1', 'J2'): total_mass_flow,
    }

    for nid, sink_data in sink_results.items():
        pipes[('J2', nid)] = sink_data['mass_flow']
        pipes[(nid, 'H')] = sink_data['mass_flow']
    return pipes