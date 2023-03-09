const net = require('net');


/*
const server = net.createServer((socket) => {
  console.log('Client connected');

  socket.on('data', (data) => {
    console.log(`Received data: ${data}`);
  });
  const num1 = 10;
  const num2 = 20;
  socket.write(`${num1},${num2}`);
});

server.listen(8010, () => {
  console.log('Server listening on port 8080');
});
*/

const client = net.createConnection({ port: 8010 }, () => {
  console.log('Connected to Python server!');

  // 发送消息给Python服务器
  // client.write('Hello from JS client!');
  const num1 = 10;
  const num2 = 20;
  client.write(`${num1},${num2}`);
});



// 监听数据事件
client.on('data', (data) => {
  console.log('Received data from Python server:', data.toString());
  client.end(); // 关闭连接
});

// 监听连接关闭事件
client.on('end', () => {
  console.log('Disconnected from Python server!');
});
