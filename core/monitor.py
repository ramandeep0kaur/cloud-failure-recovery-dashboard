import random
from core.node import get_nodes

def get_node_status():
    result = []

    for node in get_nodes():
        status = random.choice(["UP", "DOWN"])
        cpu = random.randint(10, 95)
        memory = random.randint(20, 90)

        result.append({
            "id": node["id"],
            "status": status,
            "cpu": cpu,
            "memory": memory
        })

    return result
