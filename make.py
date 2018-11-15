import os
import shutil


def build(version_name):
    docker_dir = os.path.dirname(os.path.realpath(__file__))
    try:
        shutil.rmtree(docker_dir + 'gpustat')
    except:
        pass
    shutil.copytree(docker_dir + '/../', docker_dir + 'gpustat')

    cmd = f'sudo docker build -t 192.168.50.123:5000/gpustat:{version_name} .'
    cmd += f' && sudo docker push 192.168.50.123:5000/gpustat:{version_name}'
    os.system(cmd)


if __name__ == '__main__':
    build('stable')
