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
        
        RAM.put(memory)
        end = env.now
        
        time = end - tiempo_instrucciones
        all_times.append(time)
        
        
# Ejecucion del programa
print(" ..::  Bienvenido a la simulacion de un CPU ::.." )

continuar = True
while continuar == True:
    #Pregunta por el tamaño de la RAM deseado
    print("Opciones de tamaño de RAM:  1) 100     2) 200")
    op = input("\nEscoja un tamaño de RAM:")
    if op == "1":
        size = 100
        
    elif op == "2":
        size = 200
    else:
        print("No hay opcion para ese tamaño")
        
    #Pregunta por la cantidad de procesadores que desea usar
    print("Opciones para cantidad de CPUs:  1) 1 CPU    2) 2 CPU ")
    op = input("\nEscoja una opcion:")
    if op == "1":
        cant_cpu = 1
        
    elif op == "2":
        cant_cpu = 2
    else:
        print("No hay opcion para esa cantidad")
        
    #Pregunta la cantidad de instrucciones deseada por unidad de tiempo 
    print("Opciones para cantidad de CPUs:  1) 3 instrucciones    2) 6 instrucciones ")
    op = input("\nEscoja una opcion:")
    if op == "1":
        runtime_ins = 3
        
    elif op == "2":
        runtime_ins = 6
    else:
        print("No hay opcion para esa cantidad")
        
    #Pregunta por la cantidad de procesos que desea simular
    print("Opciones para cantidad de procesos: \n")
    print(" 1) 25  2) 50  3) 100  4) 150  5) 200")
    op = input("\nEscoja una opcion:")
    if op == "1":
        cantidad_procesos = 25    
    elif op == "2":
        cantidad_procesos = 50
    elif op == "3":
        cantidad_procesos = 100
    elif op == "4":
        cantidad_procesos = 150
    elif op == "5":
        cantidad_procesos = 200
    else:
        print("No hay opcion para esa cantidad")
        
    #Pregunta el intervalo de llegada de programas que desea utilizar 
    print("Opciones de intervalos:  1) de 10   2) de 5   3) de 1 ")
    op = input("\nEscoja una opcion:")
    if op == "1":
        interval = 10
        
    elif op == "2":
        interval = 5
    
    elif op == "3":
        interval = 1
    
    else:
        print("No hay opcion para esa cantidad")
        
    continuar = False
            
                    
    
                    
    
                                           