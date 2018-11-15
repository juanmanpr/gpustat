import os


def build(version_name):
    cmd = f'sudo docker build -t 192.168.50.123:5000/gpustat:{version_name} .'
    cmd += f' && sudo docker push 192.168.50.123:5000/gpustat:{version_name}'
    os.system(cmd)
    os.system('docker run --rm --runtime=nvidia -t --pid=host -v /etc/passwd:/etc/passwd -v '
              '/var/run/docker.sock:/var/run/docker.sock 192.168.50.123:5000/gpustat:stable '
              'gpustat')

# execute with
# docker run --rm -t --runtime=nvidia -it -d --name=mygpustat --pid=host -v /etc/passwd:/etc/passwd -v /var/run/docker.sock:/var/run/docker.sock 192.168.50.123:5000/gpustat:stable
# connect with
# docker exec -it mygpustat gpustat -P


if __name__ == '__main__':
    build('stable')
