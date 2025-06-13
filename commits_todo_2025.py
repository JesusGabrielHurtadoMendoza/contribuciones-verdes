import os
import subprocess
from datetime import datetime, timedelta

# Directorio donde está tu repositorio Git
repo_dir = r'C:\Users\mm\Pictures\verde'

# Configura Git con tu nombre y correo globalmente
def configurar_git():
    subprocess.run(['git', 'config', '--global', 'user.name', 'JesusGabrielHurtadoMendoza'])
    subprocess.run(['git', 'config', '--global', 'user.email', 'jesusgabo2002@gmail.com'])

# Hacer 100 commits por cada día del rango indicado
def hacer_commits():
    os.chdir(repo_dir)
    fecha_actual = datetime(2025, 5, 9)
    fecha_final = datetime(2025, 6, 12)

    while fecha_actual <= fecha_final:
        fecha_str = fecha_actual.strftime('%Y-%m-%dT12:00:00')  # Hora fija
        for i in range(100):
            archivo_temp = f"commit_{fecha_actual.strftime('%Y%m%d')}_{i}.txt"
            with open(archivo_temp, 'w') as f:
                f.write(f"Commit {i} - {fecha_str}")
            
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = fecha_str
            env["GIT_COMMITTER_DATE"] = fecha_str

            subprocess.run(['git', 'add', archivo_temp], env=env)
            subprocess.run(['git', 'commit', '-m', f'Commit {i} en {fecha_str}'], env=env)

            os.remove(archivo_temp)

        print(f"✅ 100 commits hechos en: {fecha_actual.strftime('%Y-%m-%d')}")
        fecha_actual += timedelta(days=1)

# Subir a GitHub
def subir_a_github():
    subprocess.run(['git', 'push', 'origin', 'main'])

# Función principal
def main():
    configurar_git()
    hacer_commits()
    subir_a_github()

if __name__ == "__main__":
    main()
