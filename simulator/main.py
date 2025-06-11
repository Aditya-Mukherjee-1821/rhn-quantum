import dimod
from constants import Cp, alpha, beta
from variables import setup_vars
from bqm_builder import build_bqm
from decoder import decode_solution
from postprocess import compute_post_results, compute_pipe_flows
from network import nodes  # Import updated nodes

# Process
vars_dict = setup_vars(nodes)
bqm = build_bqm(nodes, vars_dict, alpha, beta, Cp)
response = dimod.ExactSolver().sample(bqm)
best = response.first.sample

result = decode_solution(best, vars_dict, nodes)
sink_results, heater_output = compute_post_results(result, nodes, Cp, beta)
pipes = compute_pipe_flows(sink_results)

# Output
print("Sink Results:")
for k, v in sink_results.items():
    print(f"{k}: {v}")
print("\nHeater Output:")
print(heater_output)
print("\nPipes:")
print(pipes)