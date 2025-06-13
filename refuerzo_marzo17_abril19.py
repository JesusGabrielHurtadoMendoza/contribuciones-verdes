import os
import subprocess
from datetime import datetime, timedelta

# Rango del 17 de marzo al 19 de abril de 2025
inicio = datetime.strptime("2025-05-09", "%Y-%m-%d")
fin = datetime.strptime("2025-06-12", "%Y-%m-%d")
N_COMMITS_POR_DIA = 60

def hacer_commits(fecha_str):
    for i in range(N_COMMITS_POR_DIA):
        nombre_archivo = f"refuerzo_{fecha_str.replace('-', '')}_{i}.txt"
        with open(nombre_archivo, "w") as f:
            f.write(f"Refuerzo commit {i+1} para {fecha_str}\n")

        subprocess.run(["git", "add", nombre_archivo])

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{fecha_str}T15:00:00"
        env["GIT_COMMITTER_DATE"] = f"{fecha_str}T15:00:00"

        subprocess.run(["git", "commit", "-m", f"Refuerzo commit {i+1} en {fecha_str}"], env=env)

def main():
    fecha = inicio
    while fecha <= fin:
        fecha_str = fecha.strftime("%Y-%m-%d")
        print(f"Refuerzo de {N_COMMITS_POR_DIA} commits para {fecha_str}...")
        hacer_commits(fecha_str)
        fecha += timedelta(days=1)
    print("✅ Refuerzo completado.")

if __name__ == "__main__":
    main()
