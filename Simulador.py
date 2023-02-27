import simpy
import random

def procesador(name, env, RAM, cpu, runtime_ins):
    
    start = env.now
    
    # Cantidad de memoria que ocupara el programa
    memory = random.randint(1, 10)
    print('%s esta en cola para entrar a la RAM' % (name))
    
    ins = random.randint(1, 10)
    
    # Simulacion de la memoria RAM
    with RAM.get(memory):
        
        tiempo_instrucciones = env.now
        print('%s ocupara %d MB de memoria en la RAM' % (name, memory))
        
        # Proceso donde el programa entre y se ejecuta en la CPU
        while ins > 0:
            with cpu.request() as req:
                
                print('%s se esta ejecutando en la CPU' % (name))
                
                yield req
                yield env.timeout(1)
                
                ins = ins - runtime_ins
                new_cycle = random.randint(1, 2)
                
                if new_cycle == 1:
                    yield env.timeout(2)
                elif new_cycle == 2:
                    print('%s dejo de ejecutarse en la CPU' % (name))
                    
    print("Hola")
                    
    
                                           