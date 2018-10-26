import docker
import psutil

client = docker.from_env()


def get_name_and_pids():
    list_names_pids = {}
    for container in client.containers.list():
        list_names_pids[container.attrs['State']['Pid']] = container.name
    return list_names_pids


def get_container_name(pid, names_and_pids, default_name):

    try:
        current_pid = pid
        for _ in range(10):
            new_pid = psutil.Process(current_pid).ppid()
            if current_pid == new_pid:
                raise IndexError
            try:
                return names_and_pids[new_pid]
            except KeyError:
                pass
            current_pid = new_pid
    except (IndexError, psutil.NoSuchProcess):
        return default_name
