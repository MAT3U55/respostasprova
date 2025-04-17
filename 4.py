import pandas as pd

uso_cpu = [
    [20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
    [30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
    [15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
    [10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

horas = [f"hora_{i+1}" for i in range(len(uso_cpu[0]))]

colunasi = range(len(uso_cpu))

colunasf = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1"]

cpu = pd.DataFrame(uso_cpu).T
cpu.linhas = horas
cpu.colunas = colunasf

cpu = cpu.rename(columns=dict(zip(colunasi, colunasf)))

print(cpu)