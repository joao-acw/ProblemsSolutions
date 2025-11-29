import matplotlib.pyplot as plt
import numpy as np

# 1. Dados das Tarefas
# Formato: "Nome da Tarefa: Duração Estimada: Duração Real: Dia de Conclusão"
tasks_data = """Ler manual: 1:1:3
Definir escopo do projeto: 3:4:3
Visualização do mapa: 1:3:5
artes do menu do jogo: 2:1.5:6
botoes: 2:2:8
cronograma: 2:3:9
pagina de menu: 3:2:10
integrar menu e mapa: 3:2:11
interação com o mapa: 3:4:14"""

# 2. Processamento dos Dados
# Listas para armazenar os dados processados
tasks = []
estimated_durations = []
completion_days = []

# Loop para ler cada linha dos dados e extrair as informações
for line in tasks_data.strip().split('\n'):
    try:
        # Divide a linha a partir da direita para evitar problemas com ":" no nome
        name, estimated, actual, day = line.rsplit(':', 3)
        tasks.append(name.strip())
        estimated_durations.append(float(estimated.strip()))
        completion_days.append(int(day.strip()))
    except ValueError:
        # Pula linhas que não estão no formato esperado
        print(f"Skipping malformed line: {line}")
        continue

# 3. Cálculos para o Gráfico
# Soma das durações estimadas para obter o trabalho total
total_estimated_work = sum(estimated_durations)

# Define o período do projeto (de 0 a 14 dias)
days = list(range(0, 15))
remaining_work = []

# Calcula o trabalho restante para cada dia do projeto
for day in days:
    completed_work_today = sum(estimated_durations[i] for i, d in enumerate(completion_days) if d <= day)
    remaining_work.append(total_estimated_work - completed_work_today)

# Cria a linha ideal de burndown (uma reta do trabalho total até zero)
ideal_work = np.linspace(total_estimated_work, 0, len(days))

# 4. Geração do Gráfico
# Define o tamanho da figura
plt.figure(figsize=(10, 6))

# Plota a linha do trabalho restante (real)
plt.plot(days, remaining_work, marker='o', linestyle='-', label='Trabalho Restante')

# Plota a linha de burndown ideal
plt.plot(days, ideal_work, linestyle='--', color='red', label='Linha Ideal')

# Adiciona títulos e rótulos aos eixos
plt.title('Gráfico de Burndown')
plt.xlabel('Dias')
plt.ylabel('Trabalho Restante (horas)')

# Adiciona um grid para melhor visualização
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Garante que todos os dias sejam mostrados no eixo X
plt.xticks(days)

# Salva o gráfico como um arquivo de imagem
plt.savefig('burndown_chart.png')

# Fecha a figura para liberar memória
plt.close()

print("Gráfico de burndown 'burndown_chart.png' foi gerado com sucesso!")