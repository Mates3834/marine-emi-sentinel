from simulation.run_simulation import simulate
def test_scenario():
 assert len(simulate("converter_harmonic",3)["main"])>0
