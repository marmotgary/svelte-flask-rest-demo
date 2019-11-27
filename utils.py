def parse_field_line(prefix, line):
    return line.replace(prefix, "").replace("\n", "")


def parse_desc_line(line):

    # Empty lines in field values are represented by " ."
    if line.strip() == ".":
        return "\n"
    else:
        return line


def parse_depends_line(prefix, line):
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
    package_prefix = "Package: "
    desc_prefix = "Description: "
    depends_prefix = "Depends: "
    desc_block = False
    desc_temp = ""
    package_dict = {}
    dependencies = []
    idx = 1
    pkg_name = ""

    # WORK IN PROGRESS VERSION
    with open("status.real", "r", encoding="utf8") as f:
        content = f.readlines()
        # First we map every package into a dict and assign id
        for line in content:
            if line.startswith(package_prefix):
                # package_name = line.replace(package_prefix, "").replace("\n", "")
                pkg_name = parse_field_line(package_prefix, line)
                package_dict[pkg_name] = {
                    "id": idx,
                    "description": "",
                    "description_short": "",
                    "depends": [],
                    "depends_this": []
                }
                idx += 1
            elif line.startswith(desc_prefix):
                package_dict[pkg_name]["description_short"] = parse_field_line(desc_prefix, line)
                desc_block = True
                desc_temp = ""
            elif desc_block:
                # field value lines start with a space (" ").
                if not line.startswith(" "):
                    package_dict[pkg_name]["description"] = desc_temp
                    desc_block = False
                desc_temp += parse_desc_line(line)
            elif line.startswith(depends_prefix):
                # depends_dict[package["name"]]
                pkg_depends = parse_depends_line(depends_prefix, line)
                dependencies.append({
                    "name": pkg_name,
                    "depends": pkg_depends,
                    "id": package_dict[pkg_name]["id"]
                })
        # Map each dependency to and from package (with ID id exists)
        for pkg in dependencies:
            pkg_depends = pkg["depends"]
            for pkg_d in pkg_depends:
                try:
                    id = package_dict[pkg_d]["id"]
                    package_dict[pkg_d]["depends_this"].append({"id": pkg["id"], "name": pkg["name"]})
                except KeyError:
                    id = None
                package_dict[pkg["name"]]["depends"].append({"id": id, "name": pkg_d})
    # Convert dict to list
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


def main():
    """ Main entry point of the app """
    get_packages()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
