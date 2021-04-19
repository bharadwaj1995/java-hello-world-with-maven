import docker
DOCKER_CLIENT = docker.DockerClient(base_url='unix://var/run/docker.sock')
client = docker.from_env()
RUNNING = 'running'

def create_if_not_present(container_name):
    try:
        container = DOCKER_CLIENT.containers.get(container_name)
        container_state = container.attrs['State']
        container_is_running = container_state['Status'] == RUNNING
        return container_is_running
    except:
        client.containers.run("ubuntu:latest", "echo created container")
        #client.containers.run("bharadwaj1995/poc", detach=True)
        return True
        
    

my_container_name = "asdf"
print(create_if_not_present(my_container_name))