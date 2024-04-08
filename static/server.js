// Подключение необходимых модулей
const http = require('http');
const fs = require('fs');
const path = require('path');

// Создание сервера
const server = http.createServer((req, res) => {
  // Получение пути к запрашиваемому файлу
  const filePath = path.join(__dirname, 'index.html');
  
  // Чтение HTML файла
  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(500);
      res.end('Internal Server Error');
    } else {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(content, 'utf-8');
    }
  });
});

// Запуск сервера на порту 3000
server.listen(3000, () => {
  console.log('Сервер запущен');
});
