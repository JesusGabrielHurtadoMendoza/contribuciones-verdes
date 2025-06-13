import os
import subprocess
from datetime import datetime, timedelta

# Directorio donde está tu repositorio Git
repo_dir = r'C:\Users\mm\Pictures\verde'  # Cambia esto por el path de tu repositorio

# Configura Git con tu nombre y correo
def configurar_git():
    subprocess.run(['git', 'config', '--global', 'user.name', 'JesusGabrielHurtadoMendoza'])
    subprocess.run(['git', 'config', '--global', 'user.email', 'jesusgabo2002@gmail.com'])

# Crear commits con fechas específicas
def hacer_commits():
    os.chdir(repo_dir)
    start_date = datetime(2025, 1, 1)
    today = datetime.today()

    # Realiza los commits desde enero hasta hoy
    current_date = start_date
    while current_date <= today:
        for i in range(100):  # Realiza 100 commits por día
            # Crea un archivo temporal para simular el commit
            archivo_temp = f"commit_{current_date.strftime('%Y%m%d')}_{i}.txt"
            with open(archivo_temp, 'w') as f:
                f.write(f"Commit {i} en {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Añadir el archivo y hacer commit
            subprocess.run(['git', 'add', archivo_temp])
            subprocess.run(['git', 'commit', '--date', current_date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', f'Commit {i} en {current_date.strftime("%Y-%m-%d")}'])

            # Elimina el archivo después de hacer commit
            os.remove(archivo_temp)
        
        # Incrementar un día
        current_date += timedelta(days=1)

# Función principal
def main():
    configurar_git()  # Asegúrate de configurar Git antes de hacer commits
    hacer_commits()  # Realiza los commits

if __name__ == "__main__":
    main()
