import subprocess


class SetUp:
    docker_script_to_exec = './script.sh'

    def __init__(self, image_name='dam2/mongodb_dam2', container_name='mongodb_dam2'):
        self.image_name = image_name
        self.container_name = container_name

    def _load_commands(self):
        build_image = f'docker build -t {self.image_name} .'
        run_image = f'docker run -d -p 27017:27017 --name ' \
                    f'{self.container_name} ' \
                    f'{self.image_name}'
        exec_script_in_docker_container = f'docker exec  ' \
                                          f'{self.container_name} ' \
                                          f'{self.docker_script_to_exec}'
        return build_image, run_image, exec_script_in_docker_container

    def exec_commands(self):
        command_list = self._load_commands()
        for command in command_list:
            print(f'[COMMAND]: {command} \n')
            subprocess.run(
                command, check=True,
                shell=True
            )
