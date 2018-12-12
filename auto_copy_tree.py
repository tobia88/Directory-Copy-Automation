import json, os, shutil

from pathlib import Path
from pprint import pprint

CONFIG_FILE = "config.json"

def main():
    os.chdir(Path().absolute())
    with open(CONFIG_FILE) as config:
        data = json.load(config)
        pprint(data)

        source_path = data["source_path"]
        target_dir = data["target_dir"]
        from_index = data["from_index"]
        to_index = data["to_index"]
        name_format = data["name_format"]

        for i in range(from_index, to_index + 1):
            print(i)
            copy_src_to_dest(source_path, target_dir, i, name_format)

    input("Complete, press enter to quit")


def copy_src_to_dest(spath, tpath, index, nformat):
    src = Path(spath)
    assert src.exists()

    full_path = tpath + "\\" + nformat.format(index)
    print("Copying from {0} to {1}".format(spath, full_path))

    target_dir = Path(full_path)

    if target_dir.exists():
        print("Directory {0} Existed, removing...".format(full_path))
        shutil.rmtree(full_path)

    shutil.copytree(spath, full_path)


main()