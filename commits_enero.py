import os
import subprocess
from datetime import datetime, timedelta

# Configura tus datos
REPO_DIR = r'C:\Users\mm\Pictures\verde'  # Ajusta si tu ruta cambia
USERNAME = 'JesusGabrielHurtadoMendoza'
EMAIL = 'jesusgabo2002@gmail.com'

# Comprobación del archivo index.lock
index_lock = os.path.join(REPO_DIR, '.git', 'index.lock')
if os.path.exists(index_lock):
    os.remove(index_lock)

# Configura Git
subprocess.run(['git', 'config', '--global', 'user.name', USERNAME])
subprocess.run(['git', 'config', '--global', 'user.email', EMAIL])

# Cambia al directorio del repositorio
os.chdir(REPO_DIR)

# Crear 3 commits diarios del 1 al 31 de enero
fecha = datetime(2025, 1, 1)
for dia in range(31):
    for i in range(3):
        archivo = f'enero_{fecha.strftime("%Y%m%d")}_{i}.txt'
        with open(archivo, 'w') as f:
            f.write(f'Commit del {fecha.strftime("%Y-%m-%d")} #{i}')
        
        subprocess.run(['git', 'add', archivo])

        env = os.environ.copy()
        fecha_git = fecha.strftime('%Y-%m-%dT12:00:00')
        env['GIT_COMMITTER_DATE'] = fecha_git
        env['GIT_AUTHOR_DATE'] = fecha_git

        subprocess.run(['git', 'commit', '-m', f'Commit del {fecha.strftime("%Y-%m-%d")} #{i}'], env=env)

    fecha += timedelta(days=1)
