import random

def predict(cpu, memory):
    risk = (cpu + memory) // 2
    return min(risk + random.randint(5, 15), 100)
