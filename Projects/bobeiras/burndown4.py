import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
# Movimentação de Tropas: 8:
# 1. Dados das Tarefas
# Contém APENAS as 15 tarefas da última imagem
tasks_data = """Definir Versão de Entrega: 2: 2025-10-12
Atribuição de objetivos: 5: 2025-10-20
Apresentação de acompanhamento II: 8: 2025-10-18
Visualização dos nomes do territórios: 3: 2025-10-24
Ataque: 13: 2025-10-22
Criar conjunto de objetivos disponíveis: 5: 2025-10-12
Visualização dos territórios de cada player (contorno no mapa): 8: 2025-10-21
Adicionar atributo tropas ao Território: 8: 2025-10-16
Definir custo do projeto: 4: 2025-10-19
Visualização do Objetivo: 5: 2025-10-22
Criar página de configuração da partida: 8: 2025-10-21
Distribuição de territórios por player: 8: 2025-10-23
Mudar nome dos territórios para português: 1: 2025-10-25
Integração entre botões de visualizar territórios dos players e quantidade de players: 5: 2025-10-23
"""

# 2. Definição do Período do Projeto
start_date_str = '2025-10-12' # Primeiro dia REAL do projeto
end_date_str = '2025-10-25'   # Último dia REAL do projeto

start_date = datetime.date.fromisoformat(start_date_str)
end_date = datetime.date.fromisoformat(end_date_str)

# Lista de datas REAIS do projeto (de 28/09 a 11/10)
project_dates = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Define o "Dia 0" como o dia anterior ao início
start_point_date = start_date - datetime.timedelta(days=1) # 27/09

# Lista de datas para PLOTAR (de 27/09 a 11/10)
plot_dates = [start_point_date] + project_dates

# 3. Processamento dos Dados
estimated_durations = []
completion_dates = []

for line in tasks_data.strip().split('\n'):
    try:
        parts = line.rsplit(':', 2)
        name = parts[0].strip()
        estimated = float(parts[1].strip())
        completion_str = parts[2].strip()

        estimated_durations.append(estimated)
        
        if completion_str:
            completion_dates.append(datetime.date.fromisoformat(completion_str))
        else:
            completion_dates.append(None)
            
    except (ValueError, IndexError):
        print(f"Pulando linha mal formatada: {line}")
        continue

# 4. Cálculos para o Gráfico
total_estimated_work = sum(estimated_durations)
remaining_work_corrected = []

for plot_day in plot_dates:
    if plot_day == start_point_date:
        remaining_work_corrected.append(total_estimated_work)
        continue

    completed_work_up_to_date = 0
    for i, completion_date in enumerate(completion_dates):
        if completion_date is not None and completion_date <= plot_day:
            completed_work_up_to_date += estimated_durations[i]
            
    remaining_work_corrected.append(total_estimated_work - completed_work_up_to_date)

ideal_work = np.linspace(total_estimated_work, 0, len(plot_dates))

# 5. Geração do Gráfico
plt.figure(figsize=(12, 7))

plt.plot(plot_dates, remaining_work_corrected, marker='o', linestyle='-', label='Trabalho Restante')
plt.plot(plot_dates, ideal_work, linestyle='--', color='red', label='Linha Ideal')

# Formatação dos eixos
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

# Formatação do eixo X
ax.set_xticks(project_dates)
ax.set_xlim(left=start_point_date, right=end_date)

# Formatação do eixo Y
ax.set_ylim(bottom=0, top=total_estimated_work * 1.05)

plt.gcf().autofmt_xdate()

plt.title(f'Gráfico de Burndown (Total: {total_estimated_work} horas)')
plt.xlabel('Data')
plt.ylabel('Trabalho Restante (horas)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

plt.savefig('burndown_sprint4.png')

print("Gráfico 'burndown_sprint4.png' foi gerado com sucesso!")
print(f"Total de horas estimadas (15 tarefas): {total_estimated_work}")
print("O eixo Y começa em 0 e o eixo X começa na primeira data.")