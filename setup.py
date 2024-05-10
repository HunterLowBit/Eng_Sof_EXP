import subprocess
import sys

# Instalar virtualenv
subprocess.run([sys.executable, "-m", "pip", "install", "--user", "virtualenv"])

# cria e ativa o virtual environment
subprocess.run(
    [
        sys.executable,
        "-m",
        "virtualenv",
        "--python=" + sys.executable,
        "env",
    ]
)

# ativa o virtual environment
if sys.platform == "win32":
    activate_script = ".\\env\\Scripts\\activate.bat"
else:
    activate_script = "./env/bin/activate"

subprocess.run([activate_script], shell=True)

# Instala scipy
subprocess.run(["./env/Scripts/pip", "install", "scipy"])
subprocess.run(["./env/Scripts/pip", "install", "pandas"])

# salva os pacotes instalados em requirements.txt
subprocess.run(["./env/Scripts/pip", "freeze"], stdout=open("requirements.txt", "w"))
