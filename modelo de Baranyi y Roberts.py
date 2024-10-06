import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Parámetros del modelo
N0 = 0.01  # Número inicial de células
mumax = 0.5  # Tasa específica máxima de crecimiento
K = 1.0  # Capacidad de carga del medio
h0 = 5.0  # Estado fisiológico inicial (relacionado con la fase de latencia)
t = np.linspace(0, 50, 400)  # Tiempo

# Ecuación del modelo de Baranyi y Roberts
A = t + (1 / mumax) * np.log(np.exp(-mumax * t) + np.exp(-h0) - np.exp(-mumax * t - h0))
N_t = N0 + (K - N0) * (1 - np.exp(-mumax * A))

# Graficar
plt.figure(figsize=(10, 6))
scatter = plt.scatter(t, N_t, label='Crecimiento Microbiano (Baranyi y Roberts)')
plt.xlabel('Tiempo')
plt.ylabel('Número de Células')
plt.title('Crecimiento Microbiano usando el Modelo de Baranyi y Roberts')
plt.legend()
plt.grid(True)

# Hacer los puntos seleccionables
mplcursors.cursor(scatter, hover=True)

plt.show()
