# main.py
from core.simulator import Simulator

if __name__ == "__main__":
    # Crée un simulateur à partir du fichier de configuration
    simulator = Simulator("data/network_config.json")
    
    # Lance la simulation : 60 steps (1 step = 60 seconds)
    simulator.run_simulation(n_steps=60, delta_t=60)
