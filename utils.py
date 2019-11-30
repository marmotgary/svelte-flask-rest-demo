def parse_field_line(prefix, line):
    """
    Removes prefix and line change from line
    :param prefix: is removed
    :param line: to be parsed
    :return: line with prefix and \n removed
    """
    return line.replace(prefix, "").replace("\n", "")


def parse_desc_line(line):
    """
    If empty desc row, add row changes for HTML. Otherwise remove line break.
    :param line: description row to be parsed
    :return: parsed line
    """
    # Empty lines in field values are represented by " ."
    if line.strip() == ".":
        return "<br /><br />"
    else:
        return line.replace("\n", "")


def parse_depends_line(prefix, line):
    """
    Parses dependencies from Depends value.
    :param prefix: is removed
    :param line: to be parsed
    :return: List of individual dependencies with no version number or duplicates.
    """
    line = parse_field_line(prefix, line)
    depends = []
    # Example line: libc6 (>= 2.14), zlib1g (>= 1:1.1.4), debconf (>= 0.5) | debconf-2.0
    for dependency in line.split(","):
        for depend in dependency.split("|"):
            if depend.find("(") != -1:
                # We don't need the version part of the dependency string
                depend = depend[:depend.find("(")]
            depends.append(depend.strip())
    # Return without duplicates (there may be different versions of same package)
    return list(set(depends))


def get_packages():
    """
    Reads and parses data from status.real
    :return: Alphabetically sorted list of individual packages (with name, description, dependencies)
    """
    package_prefix = "Package: "
    desc_prefix = "Description: "
    depends_prefix = "Depends: "
    desc_block = False
    desc_temp = ""
    package_dict = {}
    dependencies = []
    idx = 0
    pkg_name = ""

    # WORK IN PROGRESS VERSION
    with open("status.real", "r", encoding="utf8") as f:
        content = f.readlines()
        # First we create a dictionary of packages with IDs and list of dependencies
        for line in content:
            if line.startswith(package_prefix):
                pkg_name = parse_field_line(package_prefix, line)
                package_dict[pkg_name] = {
                    "id": idx,
                    "description": "",
                    "description_short": "",
                    "depends": [],
                    "depends_this": []
                }
                idx += 1
            # First line of Description row is a short description of the package
            elif line.startswith(desc_prefix):
                package_dict[pkg_name]["description_short"] = parse_field_line(desc_prefix, line)
                desc_block = True
                desc_temp = ""
            # Rows after the short description contains a longer description, and are prefixed with a space (" ")
            elif desc_block:
                if not line.startswith(" "):
                    package_dict[pkg_name]["description"] = desc_temp
                    desc_block = False
                desc_temp += parse_desc_line(line)
            elif line.startswith(depends_prefix):
                pkg_depends = parse_depends_line(depends_prefix, line)
                dependencies.append({
                    "name": pkg_name,
                    "depends": pkg_depends,
                    "id": package_dict[pkg_name]["id"]
                })
        # With package dictionary we can easily assign IDs to each dependency package. Assign None if package doesn't exist
        for pkg in dependencies:
            pkg_depends = pkg["depends"]
            for pkg_d in pkg_depends:
                try:
                    id = package_dict[pkg_d]["id"]
                    package_dict[pkg_d]["depends_this"].append({"id": pkg["id"], "name": pkg["name"]})
                except KeyError:
                    id = None
                package_dict[pkg["name"]]["depends"].append({"id": id, "name": pkg_d})
    # Make a list from package_dict
    packages = []
    for key, value in package_dict.items():
        package = {
            "name": key,
            "description_short": value["description_short"],
            "description": value["description"],
            "depends": value["depends"],
            "depends_this": value["depends_this"],
            "id": value["id"],
        }
        packages.append(package)
    packages = sorted(packages, key=lambda p: p["name"])
    return packages
