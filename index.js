// server.js
const express = require('express');
const app = express();
const { spawn } = require('child_process');
const path = require('path');
const bodyParser = require('body-parser');

console.log(path.join(__dirname));

// 포트 설정
const PORT = process.env.PORT || 8000;
app.use(bodyParser.json());

// 간단한 라우트
app.get('/', (req, res) => {
  res.send('Welcome to bizchat backend');
});


// refer : https://bb-library.tistory.com/214
app.post('/chat', (req, res) => {
  const sendQuestion = req.body.question;
  const execPython = path.join(__dirname, 'bizchat.py')
  const pythonPath = path.join(__dirname, "venv", "bin", "python3")
  const net = spawn(pythonPath ,[execPython, sendQuestion]);

  output = '';

  //파이썬 파일 수행 결과를 받아온다
  net.stdout.on('data', function(data) { 
    output += data.toString();
  });

  net.on('close', (code) => {
    if (code === 0) {
      res.status(200).json({ answer: output });
    } else {
      res.status(500).send('Something went wrong');
    }
  });

  net.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  })
});

// 서버 실행 
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});


