import sympy
import random
from Manager import OS as run_OS


Ram = 100
Instructions = 3
Interval = 10
Random = 130
Proocedings = 25
Num = 1

random.seed(Random)

env = sympy.Environment()
ram = sympy.Container(env, capacity=Ram, init=Ram)
cpu = sympy.Resource(env, capacity=Num)
process_times = []

def simulation():        
    
    print('- Simulación iniciada -')
    
    process_id = 0

    while process_id < Proocedings:
        process_id += 1
        next_process_time = random.expovariate(1.0 / Interval)
        yield env.timeout(next_process_time)
        run_OS(process_id, env, cpu, ram, Instructions)

env.process(simulation())
env.run()

from Statistics import showData
showData()
