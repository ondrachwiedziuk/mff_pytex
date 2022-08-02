"""Predefined packages to use, if you want to use specific modules in MFF Pytex"""


from mff_pytex.utils import command


class Package:
    def __init__(self, name: str, *params: str) -> None:
        self.name = name
        self.optional = params

    def __str__(self) -> str:
        return command('usepackage', self.name, *self.optional)


package_list: list[Package] = list()


def find_package(package: Package) -> bool:
    """Find package in package_list

    Args:
        package (Package)

    Returns:
        bool
    """
    global package_list
    for pkg in package_list:
        if pkg.name == package.name:
            return True
    return False


def add_package(*packages: Package) -> None:
    """Adds packages to package_list

    Args:
        *packages (Package): packages to add.
    """
    global package_list
    for package in packages:
        if not find_package(package):
            package_list.append(package)


def get_packages() -> list[Package]:
    """Returns package_list

    Returns:
        list[Package]: package_list
    """
    global package_list
    return package_list


def clear_packages() -> None:
    """Clears package_list
    """
    global package_list
    package_list.clear()

# TODO Autoimport packages by used environments and commands
