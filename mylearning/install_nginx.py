import os
import subprocess
from install_apache import IndexUpdater, ApacheOperations

def install_nginx():
    try:
        # Update the package list
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        
        # Create an instance of ApacheOperations to use the install_package method
        apache_ops = ApacheOperations()
        
        # Install nginx using install_package method from ApacheOperations
        apache_ops.install_package('nginx')
        
        print("Nginx installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        # Update the index.html file
        index_updater = IndexUpdater()
        index_updater.update_index_html()

if __name__ == "__main__":
    install_nginx()