import docker
DOCKER_CLIENT = docker.DockerClient(base_url='unix://var/run/docker.sock')
RUNNING = 'running'

def is_running(container_name):
    container = DOCKER_CLIENT.containers.get(container_name)

    container_state = container.attrs['State']

    container_is_running = container_state['Status'] == RUNNING

    return container_is_running

my_container_name = "asdf"
print(is_running(my_container_name))