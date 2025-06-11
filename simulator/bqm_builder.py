import dimod
from itertools import product
from helpers import int_to_bin_list

def build_bqm(nodes, vars_dict, alpha, beta, Cp):
    bqm = dimod.BinaryQuadraticModel({}, {}, 0.0, dimod.BINARY)

    for node_id, node in nodes.items():
        if node['type'] != 'sink':
            continue

        demand = node['demand']
        Ts_range = node['Ts_range']
        Tr_range = node['Tr_range']
        P_range = node['P_range']

        T_bits = vars_dict[node_id]['T_bits']
        Tr_bits = vars_dict[node_id]['Tr_bits']
        P_bits = vars_dict[node_id]['P_bits']

        for Ts_idx, Tr_idx, Ps_idx, Pr_idx in product(
            range(len(Ts_range)), range(len(Tr_range)),
            range(len(P_range)), range(len(P_range))
        ):
            Ts = Ts_range[Ts_idx]
            Tr = Tr_range[Tr_idx]
            Ps = P_range[Ps_idx]
            Pr = P_range[Pr_idx]

            if Tr >= Ts or Pr >= Ps:
                continue

            delta_T = Ts - Tr
            m = demand / (Cp * delta_T)
            cost = alpha * m * delta_T
            pressure_penalty = beta * ((Ps - Pr) ** 2)
            total_energy = cost + pressure_penalty

            sample = {}
            Ts_bin = int_to_bin_list(Ts_idx, T_bits)
            Tr_bin = int_to_bin_list(Tr_idx, Tr_bits)
            Ps_bin = int_to_bin_list(Ps_idx, P_bits)
            Pr_bin = int_to_bin_list(Pr_idx, P_bits)

            var_map = vars_dict[node_id]
            for i, b in enumerate(Ts_bin): sample[var_map['Ts'][i]] = b
            for i, b in enumerate(Tr_bin): sample[var_map['Tr'][i]] = b
            for i, b in enumerate(Ps_bin): sample[var_map['Ps'][i]] = b
            for i, b in enumerate(Pr_bin): sample[var_map['Pr'][i]] = b

            for var, val in sample.items():
                bqm.add_variable(var, 0.0)
                bqm.add_linear(var, bqm.get_linear(var) + total_energy * val)

            items = list(sample.items())
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    vi, bi = items[i]
                    vj, bj = items[j]
                    key = (vi, vj)
                    if key not in bqm.quadratic and (vj, vi) in bqm.quadratic:
                        key = (vj, vi)
                    existing = bqm.quadratic.get(key, 0.0)
                    bqm.add_quadratic(vi, vj, existing + total_energy * bi * bj)

    return bqm