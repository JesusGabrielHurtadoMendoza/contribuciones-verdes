import os
import subprocess
from datetime import datetime, timedelta
import time

# Configuración
repo_dir = r'C:\Users\mm\Pictures\verde'  # Asegúrate que esta ruta esté bien
nombre = "JesusGabrielHurtadoMendoza"
correo = "jesusgabo2002@gmail.com"

def configurar_git():
    subprocess.run(['git', 'config', '--global', 'user.name', nombre])
    subprocess.run(['git', 'config', '--global', 'user.email', correo])

def hacer_commits():
    os.chdir(repo_dir)
    fecha_actual = datetime(2025, 1, 1)
    hoy = datetime.now()

    while fecha_actual <= hoy:
        fecha_str = fecha_actual.strftime('%Y-%m-%dT12:00:00')
        for i in range(80):
            nombre_archivo = f"commit_{fecha_actual.strftime('%Y%m%d')}_{i}.txt"
            
            # Crear archivo
            with open(nombre_archivo, 'w') as f:
                f.write(f"Commit {i} del día {fecha_actual.strftime('%Y-%m-%d')}")

            subprocess.run(['git', 'add', nombre_archivo])

            # Establecer fecha personalizada
            env = os.environ.copy()
            env["GIT_COMMITTER_DATE"] = fecha_str
            env["GIT_AUTHOR_DATE"] = fecha_str

            subprocess.run(['git', 'commit', '-m', f"Commit {i} en {fecha_str}"], env=env)

            # Eliminar archivo para mantener el directorio limpio
            os.remove(nombre_archivo)

            # Pausa breve para evitar errores
            time.sleep(0.05)

        fecha_actual += timedelta(days=1)

def main():
    configurar_git()
    hacer_commits()

if __name__ == "__main__":
    main()
