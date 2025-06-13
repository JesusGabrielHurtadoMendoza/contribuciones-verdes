import os
import subprocess
from datetime import datetime

# Lista de fechas con pocos commits
fechas_objetivo = [
    "2025-04-30",
    "2025-05-01",
    "2025-05-02",
    "2025-05-03",
    "2025-05-04"
]

N_COMMITS_POR_DIA = 80

def hacer_commits(fecha_str):
    for i in range(N_COMMITS_POR_DIA):
        nombre_archivo = f"extra_{fecha_str.replace('-', '')}_{i}.txt"
        with open(nombre_archivo, "w") as f:
            f.write(f"Commit {i+1} for {fecha_str}\n")

        subprocess.run(["git", "add", nombre_archivo])

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{fecha_str}T12:00:00"
        env["GIT_COMMITTER_DATE"] = f"{fecha_str}T12:00:00"

        subprocess.run(["git", "commit", "-m", f"Extra commit {i+1} on {fecha_str}"], env=env)

def main():
    for fecha in fechas_objetivo:
        print(f"Haciendo commits para {fecha}...")
        hacer_commits(fecha)
    print("¡Todos los commits se han realizado!")

if __name__ == "__main__":
    main()
