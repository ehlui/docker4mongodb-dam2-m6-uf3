import subprocess
import unittest
import urllib.request
from setup import SetUp


# TODO trying to set another port when testing to avoid a posteriori problems
class TestSetUp(unittest.TestCase):
    mongodb_url='http://127.0.0.1:27017'
    container_name = 'mongodb_utest'
    image_name = 'mongodb_utest'

    def setUp(self) -> None:
        self.setUp = SetUp(
            image_name=self.image_name,
            container_name=self.container_name
        ).exec_commands()

    def test_continer_is_working(self):
        # TODO: Change strategy in this method
        response = urllib.request.urlopen(self.mongodb_url)
        response_data = response.read().decode()
        mongo_response = 'It looks like you are trying to ' \
                         'access MongoDB over HTTP on the' \
                         ' native driver port.'.strip()
        self.assertEqual(response_data.strip(), mongo_response)

    def tearDown(self) -> None:
        stop_container = f'docker stop {self.container_name} '
        remove_container = f'docker rm {self.container_name}'
        remove_image = f'docker rmi {self.image_name}'
        command_list = [
            stop_container, remove_container,
            remove_image
        ]
        for command in command_list:
            print(f'[COMMAND]: {command} \n')
            subprocess.run(
                command, check=True,
                shell=True
            )
        print('Both \'docker image\' and \'container\' created'
              ' during this test have been removed successfully')
