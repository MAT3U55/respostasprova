def dados_crescente(uso_regiao):
  return sorted(uso_regiao)

uso_cpu = [
    [20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
    [30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
    [15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
    [10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

for i, regiao in enumerate(uso_cpu):
  cpu_crescente = dados_crescente(regiao)
  print(f"CPU da Região {i+1}: {cpu_crescente}")