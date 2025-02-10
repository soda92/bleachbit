import contextlib
from typing import Any
import subprocess

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


@contextlib.contextmanager
def CD(d: str):
    import os

    old = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(old)


class CustomBuilder(BuildHookInterface):
    def initialize(
        self,
        version: str,  # noqa: ARG002
        build_data: dict[str, Any],
    ) -> None:
        if self.target_name == "wheel":
            return

        with CD("bleachbit_loader"):
            subprocess.run("powershell ./build.ps1".split(), check=True)
