import os


def build(version_name):
    cmd = f'sudo docker build -t 192.168.50.123:5000/gpustat:{version_name} .'
    cmd += f' && sudo docker push 192.168.50.123:5000/gpustat:{version_name}'
    os.system(cmd)


if __name__ == '__main__':
    build('stable')
