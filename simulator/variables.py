# variables.py

from helpers import bits_needed, make_vars

def setup_vars(nodes):
    vars_dict = {}
    for node_id, node in nodes.items():
        if node['type'] == 'sink':
            T_bits = bits_needed(len(node['Ts_range']))
            Tr_bits = bits_needed(len(node['Tr_range']))
            P_bits = bits_needed(len(node['P_range']))

            vars_dict[node_id] = {
                'Ts': make_vars(f'{node_id}_Ts', T_bits),
                'Tr': make_vars(f'{node_id}_Tr', Tr_bits),
                'Ps': make_vars(f'{node_id}_Ps', P_bits),
                'Pr': make_vars(f'{node_id}_Pr', P_bits),
                'T_bits': T_bits,
                'Tr_bits': Tr_bits,
                'P_bits': P_bits
            }
    return vars_dict
