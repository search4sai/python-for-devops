import subprocess
import os

class SystemOperations:
    def check_sudo(self):
        """
        Checks if the script is run with sudo.
        """
        if os.geteuid() != 0:
            print("Please run this script with sudo.")
            return False
        return True

class ApacheOperations:
    def update_apt(self):
        """
        Updates the apt package list using sudo.
        """
        try:
            # Run the apt update command
            result = subprocess.run(["apt", "update"], capture_output=True, text=True, check=True)
            print("APT Update Successful")
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print(f"APT Update Failed. Error:\n{e.stderr}")
        except OSError as e:
            print(f"Failed to run apt update. Error:\n{e}")

    def install_package(self, package_name):
        """
        Installs a package using apt-get install with sudo.
        Args:
            package_name (str): The name of the package to install.
        """
        try:
            # Run the apt-get install command
            result = subprocess.run(["apt-get", "install", "-y", package_name], capture_output=True, text=True, check=True)
            print(f"Successfully installed {package_name}")
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package_name}. Error:\n{e.stderr}")
        except OSError as e:
            print(f"Failed to run apt-get install. Error:\n{e}")

    def check_apache_status(self):
        """
        Checks the status of the Apache service using systemctl.
        """
        try:
            # Run the systemctl status apache2 command
            result = subprocess.run(["systemctl", "status", "apache2"], capture_output=True, text=True, check=True)
            print("Apache Status:")
            print(result.stdout)

            # Check if Apache is running
            if "active (running)" not in result.stdout:
                print("Apache is not running. Restarting the service...")
                self.restart_apache()
            else:
                print("Apache is running.")

        except subprocess.CalledProcessError as e:
            print(f"Failed to check Apache status. Error:\n{e.stderr}")
        except OSError as e:
            print(f"Failed to run systemctl status apache2. Error:\n{e}")

    def restart_apache(self):
        """
        Restarts the Apache service.
        """
        try:
            # Restart the Apache service
            subprocess.run(["systemctl", "restart", "apache2.service"], check=True)
            print("Apache service restarted successfully.")
            IndexUpdater().update_index_html()

        except subprocess.CalledProcessError as e:
            print(f"Failed to restart Apache service. Error:\n{e.stderr}")

class IndexUpdater:
    def update_index_html(self):
        """
        Updates the index.html file.
        """
        try:
            # Update the index.html file
            with open("/var/www/html/index.html", "w") as file:
                file.write("<html><body><h1>Welcome to Hello World</h1></body></html>")
            print("Updated index.html with 'Welcome to Hello World'.")

        except OSError as e:
            print(f"Failed to update index.html. Error:\n{e}")

if __name__ == "__main__":
    system_ops = SystemOperations()
    apache_ops = ApacheOperations()

    if system_ops.check_sudo():
        apache_ops.update_apt()
        apache_ops.install_package("apache2")
        apache_ops.check_apache_status()