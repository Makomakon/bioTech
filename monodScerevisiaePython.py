import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mplcursors

# Parámetros y valores iniciales
umax = 0.4  # h^-1
umax2 = 0.2
Yxs = 0.47  # g/g
Yps = 0.43  # g/g
Ksx = 237  # g/L
qpmax = 1.25
Ksp = 323  # g/L
Pmax = 45

X0 = 3  # Biomasa inicial g/L
P0 = 0  # Etanol inicial en g/L
S0 = 60  # Concentración de sustrato inicial g/L

# Fermentación primaria
def fder(C, t):
    X, P, S = C
    u = (umax * S) / (Ksx + S)
    dXdt = u * X
    dPdt = qpmax * (S / (Ksp + S)) * X * (1 - P / Pmax)
    dSdt = -(dXdt / Yxs) - (dPdt / Yps)
    
    if S < 0.19 * S0:  # Extent 81%
        u = 0
        dPdt = 0
        dSdt = 0
    if X > 97.5:  # [X] máxima
        dXdt = 0
    
    return [dXdt, dPdt, dSdt]

tode = np.linspace(0, 72, 150)
C0 = [X0, P0, S0]
Conc = odeint(fder, C0, tode)

# Fermentación secundaria
def fder2(C2, t):
    X, P, S = C2
    u = (umax2 * S) / (Ksx + S)
    dXdt = u * X
    dPdt = qpmax * (S / (Ksp + S)) * X * (1 - P / Pmax)
    dSdt = -(dXdt / Yxs) - (dPdt / Yps)
    
    if S < 0.19 * Conc[-1, 2]:  # Extent 81%
        u = 0
        dXdt = 0
        dPdt = 0
        dSdt = 0
    if X > 97.5:  # [X] máxima
        dXdt = 0
    
    return [dXdt, dPdt, dSdt]

Cf = Conc[-1, :]
Conc2 = odeint(fder2, Cf, tode)

# Gráficos
# Fermentación primaria
plt.figure()
plt.plot(tode, Conc[:, 2], 'g-', linewidth=2, label='Sustrato')
plt.plot(tode, Conc[:, 0], color='orange', linestyle='-', linewidth=2, label='Biomasa')
plt.plot(tode, Conc[:, 1], color='red', linestyle='-', linewidth=2, label='Etanol')
plt.grid(True)
plt.title('Fermentación primaria S. cerevisiae')
plt.legend()
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/L)')
plt.axis([0, 72, 0, 100])  # Ajuste de límite superior
mplcursors.cursor(hover=True)

# Fermentación secundaria
plt.figure()
plt.plot(tode, Conc2[:, 2], 'g-', linewidth=2, label='Sustrato')
plt.plot(tode, Conc2[:, 0], color='orange', linestyle='-', linewidth=2, label='Biomasa')
plt.plot(tode, Conc2[:, 1], color='red', linestyle='-', linewidth=2, label='Etanol')
plt.grid(True)
plt.title('Fermentación secundaria S. cerevisiae')
plt.legend()
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/L)')
plt.axis([0, 50, 0, 100])  # Ajuste de límite superior
mplcursors.cursor(hover=True)

# Ambas fermentaciones
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(tode, Conc[:, 2], 'g-', linewidth=2, label='Sustrato')
plt.plot(tode, Conc[:, 0], color='orange', linestyle='-', linewidth=2, label='Biomasa')
plt.plot(tode, Conc[:, 1], color='red', linestyle='-', linewidth=2, label='Etanol')
plt.grid(True)
plt.title('Fermentación primaria S.c.')
plt.legend()
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/L)')
plt.axis([0, 50, 0, 60])
mplcursors.cursor(hover=True)

plt.subplot(1, 2, 2)
plt.plot(tode, Conc2[:, 2], 'g-', linewidth=2, label='Sustrato')
plt.plot(tode, Conc2[:, 0], color='orange', linestyle='-', linewidth=2, label='Biomasa')
plt.plot(tode, Conc2[:, 1], color='red', linestyle='-', linewidth=2, label='Etanol')
plt.grid(True)
plt.title('Fermentación secundaria S.c.')
plt.legend()
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/L)')
plt.axis([0, 50, 0, 60])
mplcursors.cursor(hover=True)

# Comparativa
plt.figure()
plt.plot(tode, Conc[:, 2], color='cyan', linestyle='-', linewidth=2, label='Sustrato primaria')
plt.plot(tode, Conc[:, 0], color='cyan', linestyle='--', linewidth=2, label='Biomasa primaria')
plt.plot(tode, Conc[:, 1], color='cyan', linestyle='-.', linewidth=2, label='Etanol primaria')

plt.plot(tode, Conc2[:, 2], color='orange', linestyle='-', linewidth=2, label='Sustrato secundaria')
plt.plot(tode, Conc2[:, 0], color='orange', linestyle='--', linewidth=2, label='Biomasa secundaria')
plt.plot(tode, Conc2[:, 1], color='orange', linestyle='-.', linewidth=2, label='Etanol secundaria')

plt.grid(True)
plt.title('Comparativa de las fermentaciones')
plt.legend(['Sustrato primaria', 'Biomasa primaria', 'Etanol primaria', 'Sustrato secundaria', 'Biomasa secundaria', 'Etanol secundaria'])
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/L)')
plt.axis([0, 50, 0, 60])
mplcursors.cursor(hover=True)

Cf2 = Conc2[-1, :]
plt.show()
