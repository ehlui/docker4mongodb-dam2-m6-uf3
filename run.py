from setup import SetUp

if __name__ == '__main__':
    SetUp(
        image_name='dam2-mongodb-ehlui',
        container_name='dam2-mongodb-server'
    ).exec_commands()
