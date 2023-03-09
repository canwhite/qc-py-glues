#先把和js通信做完

import socket
import json
import subprocess

HOST = 'localhost'
PORT = 8010


#接收到值之后执行java方法

def add(a, b):
    # 编译Java代码
    subprocess.call(['javac', 'Calculator.java'])

    # 调用Java方法
    p = subprocess.Popen(['java', 'Calculator'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    input_str = f'{a} {b}\n'
    output_str, _ = p.communicate(input_str.encode('utf-8'))
    result = int(output_str.decode('utf-8').strip())

    return result


# 这部分是js建立socket，然后py建立socket联系js，我们需要颠倒过来

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024) #接收值用

    # 接收值
    nums = data.decode().split(',')
    num1 = int(nums[0])
    num2 = int(nums[1])



    result = add(num1,num2);
    s.sendall(str(result).encode())



print('Received data:', data.decode())
'''


# 创建TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_socket.bind(('localhost', 8010))

# 监听连接请求
server_socket.listen()


# 处理连接
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    # 发送消息给客户端
    # message = "Hello from Python server!"
    # client_socket.send(message.encode())

    # 接收消息
    data = client_socket.recv(1024)
    nums = data.decode().split(',')
    num1 = int(nums[0])
    num2 = int(nums[1])


    result = add(num1,num2);
    client_socket.sendall(str(result).encode())

    # 关闭连接
    # client_socket.close()