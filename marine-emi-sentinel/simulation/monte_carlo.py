
from .run_simulation import simulate
def run_monte_carlo(scenarios,n_runs=20,base_seed=100):
    return [{"scenario":s,"seed":base_seed+i,"features":simulate(s,base_seed+i)["features"]["kalman"]}
            for s in scenarios for i in range(n_runs)]
