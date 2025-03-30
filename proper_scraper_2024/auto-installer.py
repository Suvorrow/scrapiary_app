import pathlib
import shutil
import subprocess
import shlex
from make_directory import path_list


def is_package_installed(package_name: str, default_path: str = "") -> bool:
    package_exist: str | None = shutil.which(package_name)
    default_path_ = pathlib.Path(default_path)
    default_path_exist: bool = (default_path_.exists() if default_path_ else False)
    if package_exist or default_path_exist:
        print(f"Package {package_name} is installed. ")
        return True
    return False


def run_install_queries(instructions_install: dict[str, str]) -> None:
    for key_name, instruction in instructions_install.items():
        try:
            __execute_package_install(instruction, key_name)
        except Exception as error:
            print(f"Error: Failed to execute '{key_name}': {error}. ")
            return


def __execute_package_install(instruction_: str, key_name_: str) -> None:
    workdir = path_list[6]
    try:
        subprocess.run(
            shlex.split(instruction_),
            cwd=workdir,
            capture_output=True,
            check=True,
        )
        print(f"{key_name_} has been installed successfully ")
        return
    except subprocess.CalledProcessError as error:
        print(f"Error: failed to install {error} ")


def install_docker() -> None:
    if is_package_installed("docker"):
        print(f"It's had installed. ")
        return
    curl_queries: dict[str, str] = {
        "Update packages": "sudo apt update -y",
        "Pre-requisite packages":
            "sudo apt install -y apt-transport-https ca-certificates curl software-properties-common",
        "Docker GPG Key":
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | "
            "sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",
        "Docker Repository":
            "echo 'deb, [arch=$(dpkg --print-architecture), signed-by=/usr/share/keyrings/docker-archive-keyring.gpg]' "
            "'https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' | "
            "sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
        "Docker": "sudo apt install -y docker-ce containerd.io"
    }
    try:
        run_install_queries(curl_queries)
    except Exception as error:
        print(f"{error}. ")
        return
    return


if __name__ == "__main__":
    install_docker()

