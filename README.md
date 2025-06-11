# rhn_bqm
This repository contains a very basic implementation of an RHN network solved using Dwave's dimod library, using BQM formulation.

The code optimizes the cost of production based on per watt energy prices. I also ensures that the temperatures are well withing the specified ranges as well as the differential pressure between twin pipes are as close to zero.

This repository contains a structured code to optimize heater costs in district heating network using BQM formulation of the problem statement. The optimization function of the same uses heater production cost, differential pressures across twin pipes. The optimizer ensures each and every demand of consumer is always met.
