// server.js
const express = require('express');
const app = express();
const { spawn } = require('child_process');
const path = require('path');
const bodyParser = require('body-parser');

console.log(path.join(__dirname));


// os.environ['USER_AGENT'] = 'myagent'
// 포트 설정
const PORT = process.env.PORT || 8080;
app.use(bodyParser.json());

// 간단한 라우트
app.get('/', (req, res) => {
  res.send('Welcome to bizchat backend');
});

// '/weather' 경로에 대한 GET 요청을 처리하는 핸들러
app.get('/weather', (req, res) => {
  try {
    // EC2 서버에서 현재 실행 중인 Node.js 파일의 절대 경로를 기준으로 설정합니다.
    const scriptPath = path.join(__dirname, 'weather.py');
    const pythonPath = path.join(__dirname, 'venv', 'bin', 'python3');


    // Spawn the Python process with the correct argument
    const result = spawn(pythonPath, [scriptPath]);

    let responseData = '';

    // Listen for data from the Python script
    result.stdout.on('data', (data) => {
      // console.log(data.toString());
      // res.status(200).json({ answer: data.toString() });
      responseData += data.toString();
    });


    // Listen for errors from the Python script
    result.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      res.status(500).json({ error: data.toString() });
    });


    // Handle the close event of the child process
    result.on('close', (code) => {
      if (code === 0) {
        res.status(200).json({ answer: responseData });
      } else {
        res
          .status(500)
          .json({ error: `Child process exited with code ${code}` });
      }
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }

});


// refer : https://bb-library.tistory.com/214
app.post('/chat', (req, res) => {
  try {
    const sendedQuestion = req.body.question;


    // EC2 서버에서 현재 실행 중인 Node.js 파일의 절대 경로를 기준으로 설정합니다.
    const scriptPath = path.join(__dirname, 'bizchat.py');
    const pythonPath = path.join(__dirname, 'venv', 'bin', 'python3');


    // Spawn the Python process with the correct argument
    const result = spawn(pythonPath, [scriptPath, sendedQuestion]);


    let responseData = '';


    // Listen for data from the Python script
    result.stdout.on('data', (data) => {
      // console.log(data.toString());
      // res.status(200).json({ answer: data.toString() });
      responseData += data.toString();
    });


    // Listen for errors from the Python script
    result.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      res.status(500).json({ error: data.toString() });
    });


    // Handle the close event of the child process
    result.on('close', (code) => {
      if (code === 0) {
        res.status(200).json({ answer: responseData });
      } else {
        res
          .status(500)
          .json({ error: `Child process exited with code ${code}` });
      }
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

// refer : https://bb-library.tistory.com/214
app.post('/recommend', (req, res) => {
  try {
    const sendedQuestion = req.body.question;


    // EC2 서버에서 현재 실행 중인 Node.js 파일의 절대 경로를 기준으로 설정합니다.
    const scriptPath = path.join(__dirname, 'recommend.py');
    const pythonPath = path.join(__dirname, 'venv', 'bin', 'python3');


    // Spawn the Python process with the correct argument
    const result = spawn(pythonPath, [scriptPath, sendedQuestion]);


    let responseData = '';


    // Listen for data from the Python script
    result.stdout.on('data', (data) => {
      // console.log(data.toString());
      // res.status(200).json({ answer: data.toString() });
      responseData += data.toString();
    });


    // Listen for errors from the Python script
    result.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      res.status(500).json({ error: data.toString() });
    });


    // Handle the close event of the child process
    result.on('close', (code) => {
      if (code === 0) {
        res.status(200).json({ answer: responseData });
      } else {
        res
          .status(500)
          .json({ error: `Child process exited with code ${code}` });
      }
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

// 서버 실행 
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});


