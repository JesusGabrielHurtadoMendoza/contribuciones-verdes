import os
import subprocess
from datetime import datetime, timedelta

# Fechas desde el 27 de enero al 6 de febrero de 2025
inicio = datetime.strptime("2025-01-27", "%Y-%m-%d")
fin = datetime.strptime("2025-02-06", "%Y-%m-%d")
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
    fecha = inicio
    while fecha <= fin:
        fecha_str = fecha.strftime("%Y-%m-%d")
        print(f"Haciendo commits para {fecha_str}...")
        hacer_commits(fecha_str)
        fecha += timedelta(days=1)
    print("¡Todos los commits se han realizado!")

if __name__ == "__main__":
    main()
