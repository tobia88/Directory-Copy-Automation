import json
import os
import shutil
import traceback
import logging

from pathlib import Path
from pprint import pprint

CONFIG_FILE = "config.json"


def main():
    try:
        with open(CONFIG_FILE) as config:
            data = json.load(config)
            pprint(data)

            source_path = data["source_path"]
            target_dir = data["target_dir"]
            from_index = data["from_index"]
            to_index = data["to_index"]
            name_format = data["name_format"]
            keep_file = data["keep_file"]

            for i in range(from_index, to_index + 1):
                print(i)
                copy_src_to_dest(source_path, target_dir,
                                i, name_format, keep_file)

    except Exception:
        logging.error(traceback.format_exc())

    input("Complete, press enter to quit")


def copy_src_to_dest(spath, tpath, index, nformat, sfile_name):
    src = Path(spath)
    assert src.exists()

    full_path = tpath + "\\" + nformat.format(index)
    print("Copying from {0} to {1}".format(spath, full_path))

    target_dir = Path(full_path)
    tmp_path = tpath + "//" + sfile_name

    if target_dir.exists():
        file_path = Path(full_path + "//" + sfile_name)

        if file_path.exists() and file_path.is_file():
            print(sfile_name + " existed, making backup...")
            shutil.copyfile(file_path.absolute(), tmp_path)

        print("Directory {0} Existed, removing...".format(full_path))
        shutil.rmtree(full_path)

    shutil.copytree(spath, full_path)

    if Path(tmp_path).exists():
        print("Paste {0} to {1}".format(tmp_path, full_path))
        shutil.copyfile(tmp_path, full_path + "//game.txt")
        print("Complete Paste, removing {0}".format(tmp_path))
        os.remove(tmp_path)


main()
