from helpers import bin_list_to_int

def decode_solution(best, vars_dict, nodes):
    result = {}
    for node_id in vars_dict:
        vmap = vars_dict[node_id]
        Ts_idx = bin_list_to_int([best[v] for v in vmap['Ts']])
        Tr_idx = bin_list_to_int([best[v] for v in vmap['Tr']])
        Ps_idx = bin_list_to_int([best[v] for v in vmap['Ps']])
        Pr_idx = bin_list_to_int([best[v] for v in vmap['Pr']])

        result[node_id] = {
            'Ts': nodes[node_id]['Ts_range'][Ts_idx],
            'Tr': nodes[node_id]['Tr_range'][Tr_idx],
            'Ps': nodes[node_id]['P_range'][Ps_idx],
            'Pr': nodes[node_id]['P_range'][Pr_idx]
        }
    return result
