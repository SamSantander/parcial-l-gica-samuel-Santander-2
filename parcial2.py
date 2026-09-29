import networkx as nx
import matplotlib.pyplot as plt

# 1. creado
G = nx.Graph()

# 2. conexiones
conexiones = [
    # Familia / Relaciones
    ("Samuel Alejandro", "Mamá"), 
    ("Samuel Alejandro", "Papá"), 
    ("Samuel Alejandro", "Novia"),
    
    # Amigos del barrio / Hobbies
    ("Samuel Alejandro", "Amigo Valorant"), 
    ("Samuel Alejandro", "Amiga Bolirana"), 
    ("Amigo Valorant", "Amiga Bolirana"), # Conexión entre ellos
    
    # Universidad
    ("Samuel Alejandro", "Compañero 1 (La Salle)"), 
    ("Samuel Alejandro", "Compañero 2 (La Salle)")
]

# Agregar
G.add_edges_from(conexiones)

# Dibujar 
plt.figure(figsize=(9, 6))
nx.draw(G, with_labels=True, node_color="skyblue", node_size=3500, font_size=9, font_weight="bold", edge_color="gray")


plt.title("Mi Red Social")
plt.show()