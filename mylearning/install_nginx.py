import os
import subprocess
from install_apache import IndexUpdater
from install_apache import install_package

def install_nginx():
    try:
        # Update the package list
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        
        # Install nginx using install_package function from install_apache
        install_package('nginx')
        
        print("Nginx installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        # Update the index.html file
        index_updater = IndexUpdater()
        index_updater.update_index()
if __name__ == "__main__":
    install_nginx()