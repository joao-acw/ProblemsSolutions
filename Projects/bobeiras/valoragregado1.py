import matplotlib.pyplot as plt
import numpy as np


semana_atual = 9
total_semanas = 14

semanas = list(range(1, total_semanas + 1))

pv_semanal = [3, 18, 13, 28, 52, 37, 17, 13, 28, 21, 56, 29, 10, 8]


ac_semanal_parcial = [6, 22, 16]
ev_semanal_parcial = [3, 18, 13]

ac_semanal = ac_semanal_parcial + [np.nan] * (total_semanas - semana_atual)
ev_semanal = ev_semanal_parcial + [np.nan] * (total_semanas - semana_atual)

pv_acumulado = np.cumsum(pv_semanal)
ac_acumulado = np.cumsum(ac_semanal) 
ev_acumulado = np.cumsum(ev_semanal)


semanas_plot = [0] + semanas
pv_plot = np.insert(pv_acumulado, 0, 0)
ac_plot = np.insert(ac_acumulado, 0, 0)
ev_plot = np.insert(ev_acumulado, 0, 0)


plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 8)) 

ax.plot(semanas_plot, pv_plot, marker='o', linestyle='--', color='blue',
        label='PV (Valor Planejado)', linewidth=2.5, markersize=8, alpha=0.9)
ax.plot(semanas_plot, ac_plot, marker='s', linestyle='-', color='red',
        label='AC (Custo Real)', linewidth=2.5, markersize=8, alpha=0.9)
ax.plot(semanas_plot, ev_plot, marker='^', linestyle='-', color='green',
        label='EV (Valor Agregado)', linewidth=2.5, markersize=8, alpha=0.9)

ax.axvline(x=semana_atual, color='gray', linestyle='-.', linewidth=1.5,
           label=f'Status na Semana {semana_atual}')

ax.set_title(f'Gráfico de Valor Agregado', fontsize=18, pad=20)
ax.set_xlabel('Semanas', fontsize=14, labelpad=15)
ax.set_ylabel('Valor Acumulado (Horas)', fontsize=14, labelpad=15)
ax.legend(fontsize=12, loc='upper left') 
ax.grid(True, linestyle=':', alpha=0.7) 


plt.xticks(list(range(0, total_semanas + 1, 1)), fontsize=10) 
plt.yticks(fontsize=10)


max_y_value = max(np.nanmax(pv_plot), np.nanmax(ac_plot), np.nanmax(ev_plot))
ax.set_ylim(bottom=-5, top=max_y_value * 1.10) 
plt.tight_layout()
plt.savefig('valor_agregado_chart.png')