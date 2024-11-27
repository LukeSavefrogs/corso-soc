import platform
import pathlib

import textwrap

if __name__ == '__main__':
    # if platform.system() != "Linux":
    #     print("Questo script è stato pensato per essere eseguito su un sistema Linux.")
    #     exit(1)

    target_path = "~/../"
    target_glob = "**/.ssh/id_*"

    script_content = f"""
        \"\"\"Questo file e' stato generato dinamicamente dallo script 'remote.py'\"\"\"
        import pathlib

        if __name__ == '__main__':
            print([
                str(file.resolve())
                for file in pathlib.Path("{target_path}").expanduser().glob("{target_glob}")
            ])
    """

    parent_folder = pathlib.Path(__file__).parent
    (parent_folder / "dynamic_script.py").write_text(textwrap.dedent(script_content))