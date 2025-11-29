import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick


semana_atual = 8
total_semanas = 14
custo_por_hora = 10

semanas = list(range(1, total_semanas + 1))

pv_semanal = [3, 18, 13, 28, 52, 37, 17, 13, 28, 21, 56, 29, 10, 8]
ac_semanal_parcial = [6, 22, 16, 30, 40, 26, 25, 30]
ev_semanal_parcial = [3, 18, 13, 36, 52, 34, 25, 44]

ac_semanal = ac_semanal_parcial + [np.nan] * (total_semanas - semana_atual)
ev_semanal = ev_semanal_parcial + [np.nan] * (total_semanas - semana_atual)

pv_acumulado_horas = np.cumsum(pv_semanal)
ac_acumulado_horas = np.cumsum(ac_semanal)
ev_acumulado_horas = np.cumsum(ev_semanal)

pv_acumulado_reais = pv_acumulado_horas * custo_por_hora
ac_acumulado_reais = ac_acumulado_horas * custo_por_hora
ev_acumulado_reais = ev_acumulado_horas * custo_por_hora

semanas_plot = [0] + semanas
pv_plot = np.insert(pv_acumulado_reais, 0, 0)
ac_plot = np.insert(ac_acumulado_reais, 0, 0)
ev_plot = np.insert(ev_acumulado_reais, 0, 0)

print("PV Acumulado (R$):", pv_acumulado_reais[7])
print("AC Acumulado (R$):", ac_acumulado_reais[7])
print("EV Acumulado (R$):", ev_acumulado_reais[7])

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

ax.set_title(f'Gráfico de Valor Agregado (EVA)', fontsize=18, pad=20)
ax.set_xlabel('Semanas', fontsize=14, labelpad=15)
ax.set_ylabel('Valor Acumulado (R$ Reais)', fontsize=14, labelpad=15)
ax.legend(fontsize=12, loc='upper left')
ax.grid(True, linestyle=':', alpha=0.7)


plt.xticks(list(range(0, total_semanas + 1, 1)), fontsize=10)
plt.yticks(fontsize=10)

fmt = 'R${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

max_y_value = max(np.nanmax(pv_plot), np.nanmax(ac_plot), np.nanmax(ev_plot))
ax.set_ylim(bottom=-5, top=max_y_value * 1.10)
plt.tight_layout()
plt.savefig('valor_agregado_2.png')
