import sympy
from random import seed as configure_seed
import Statistics 
from Prooceding import Prooceding
from random import rand


class OS:
    def __init__( env, ram, cpu, prooceding_id, instructions, self):
    
        self.instructions = instructions
        self.prooceding_id = prooceding_id
        self.env = env
        self.ram = ram
        self.cpu = cpu
        env.process(self.run())

    def run(self):
        
        stime = self._currentTime()

       
        memorys = rand(1, 10)
        instruction = rand(1, 10)
        prooceding = Prooceding(self.prooceding_id, memorys, instruction)

        print(f' time {self._currentTime()}: Process {process.id} (new)')

        
        with self.ram.get(process.memory) as ramRequest:
            yield ramRequest
            print(
                f'  time {self._currentTime()}: Process {process.id} (ready)')

          
            cycle = 0
            while process.instructions > 0:
                with self.cpu.request() as cpuRequest:
                    yield cpuRequest
                    cycle =+ 1
                    print(
                        f'  time {self._currentTime()}: Process {process.id} (Running Cycle {cycle})')
                  
                    if process.instructions == 0:
                        print(
                            f'  Time {self._currentTime()}: Process {process.id} (Terminated)')

                    else:
                        
                        next = rand(1, 2)