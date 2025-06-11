# network.py

nodes = {
    'H': {'type': 'heater'},

    'J1': {'type': 'junction'},
    'J2': {'type': 'junction'},

    'S1': {
        'type': 'sink',
        'Ts_range': [70, 72, 74],
        'Tr_range': [38, 40, 42],
        'P_range': [8, 9, 10, 11],
        'demand': 500
    },
    'S2': {
        'type': 'sink',
        'Ts_range': [78, 80, 82],
        'Tr_range': [58, 60, 62],
        'P_range': [8, 9, 10, 11],
        'demand': 300
    },
    'S3': {
        'type': 'sink',
        'Ts_range': [65, 67, 69],
        'Tr_range': [40, 42, 44],
        'P_range': [8, 9, 10, 11],
        'demand': 200
    }
}

# Define bidirectional edges (supply + return)
supply_edges = [
    ('H', 'J1'),
    ('J1', 'J2'),
    ('J2', 'S1'),
    ('J2', 'S2'),
    ('J1', 'S3')
]

# Generate return edges as the reverse of each supply edge
return_edges = [(b, a) for (a, b) in supply_edges]

# Full bidirectional network
edges = supply_edges + return_edges
