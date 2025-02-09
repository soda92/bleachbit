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
venv_path = CURRENT.parent.joinpath("bleachbit_venv")


def create_shortcut():
    import winshell

    winshell.CreateShortcut(
        Path=str_path(Path(winshell.desktop()).joinpath("BleachBit (New).lnk")),
        Target=r"C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe",
        Arguments=str_path(CURRENT.joinpath("launcher.ps1")),
        Icon=[str_path(CURRENT.joinpath("bleachbit.ico")), 0],
        Description="Clean Your System and Free Disk Space.",
    )
    pass


def main():
    if not venv_path.exists():
        with CD(CURRENT.parent):
            subprocess.run("msys2_env --init".split(), check=True)
            subprocess.run("msys2_env --venv bleachbit_venv".split(), check=True)
    p = "ucrt64/mingw-w64-ucrt-x86_64-"
    subprocess.run(
        [
            "powershell.exe",
            str_path(venv_path.joinpath("bin/fish.ps1")),
            "-c",
            f"'pacman -S --noconfirm --needed {p}python-gobject {p}gtk3 {p}python-pywin32'",
        ],
        check=True,
    )
    create_shortcut()
    with CD(CURRENT):
        subprocess.run(
            [str_path(venv_path.joinpath("bin/python.exe")), "impl.py"], check=True
        )


if __name__ == "__main__":
    main()
