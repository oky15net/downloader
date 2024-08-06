# install.py
import subprocess

def install():
    subprocess.check_call(["pip", "install", "requests"])

if __name__ == "__main__":
    install()
