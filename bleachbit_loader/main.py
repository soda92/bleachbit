from pathlib import Path
import contextlib
import os
import subprocess


@contextlib.contextmanager
def CD(d: Path):
    old = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(old)


def str_path(p: Path):
    p = p.resolve()
    return str(p).replace("\\", "/")


CURRENT = Path(__file__).resolve().parent


def main():
    venv_path = CURRENT.parent.joinpath("bleachbit_venv")
    if not venv_path.exists():
        with CD(CURRENT.parent):
            subprocess.run("msys2_env --init".split(), check=True)
            subprocess.run("msys2_env --venv bleachbit_venv".split(), check=True)
    p = "ucrt64/mingw-w64-ucrt-x86_64-"
    subprocess.run(
        [
            venv_path.joinpath("bin/fish.ps1"),
            "-c",
            f"pacman -S --noconfirm --needed {p}python-gobject {p}gtk3",
        ],
        check=True,
    )
    with CD(CURRENT):
        subprocess.run(
            [str_path(venv_path.joinpath("bin/python.exe")), "impl.py"], check=True
        )


if __name__ == "__main__":
    main()
