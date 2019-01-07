import docker
import psutil

client = docker.from_env()


# when default pid
def get_name_and_pids_method1():
    list_names_pids = {}
    for container in client.containers.list():
        list_names_pids[container.attrs['State']['Pid']] = container.name
    return list_names_pids


def get_container_name_method1(pid, names_and_pids, default_name):
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


# when pid=host
def get_name_and_pids_method2():
    list_names_pids = {}
    for container in client.containers.list():
        list_pids = [int(x[1]) for x in container.top()['Processes']]
        list_names_pids[container.name] = list_pids
    return list_names_pids


def get_container_name_method2(pid, names_and_pids, default_name):
    pid = int(pid)
    for name, pids in names_and_pids.items():
        if pid in pids:
            return name
    else:
        return default_name
