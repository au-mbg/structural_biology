# List all packages available in the current Python environment
import pkg_resources
def list_installed_packages():
    installed_packages = pkg_resources.working_set
    package_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    return package_list

for package in list_installed_packages():
    print(package)