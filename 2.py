def alerta_uso(uso_regiao):
  for uso in uso_regiao:
    if uso > 85:
      return True
  return False

uso_cpu = [
    [20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
    [30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
    [15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
    [10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

for i, regiao in enumerate(uso_cpu):
  if alerta_uso(regiao):
    print(f"CPU alta na região {i+1}")
  else:
    print(f"CPU Normal na Região {i+1}")