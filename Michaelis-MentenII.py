import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Parámetros
V_max = 1.0  # Velocidad máxima
K_m = 0.5  # Constante de Michaelis
S = np.linspace(0, 10, 100)  # Concentración de sustrato

# Ecuación de Michaelis-Menten
v = (V_max * S) / (K_m + S)

# Graficar
plt.figure(figsize=(15, 6))
scatter = plt.scatter(S, v, label='Cinética de Michaelis-Menten')
plt.xlabel('Concentración de Sustrato [S]')
plt.ylabel('Velocidad de la Reacción [v]')
plt.title('Cinética de Michaelis-Menten')
plt.legend()
plt.grid(True)

# Agregar puntos Vmax Vmax/2 y Km
plt.axhline(y=V_max/2, color='r', linestyle='--', label='$V_{max}/2$')
plt.axvline(x=K_m, color='g', linestyle='--', label='$K_m$')
plt.scatter([K_m], [V_max/2], color='orange')  # Punto de intersección
plt.axhline(y=V_max,color='g', linestyle='dotted', label='V_max')

# Hacer los puntos seleccionables
mplcursors.cursor(scatter, hover=True)

plt.legend()
plt.show()
