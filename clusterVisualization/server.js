var express = require('express'),
  app = express();

app.get('/', function (req, res) {
  res.sendfile('index.html');
});

app.get('/worldNews.json', function (req, res) {
  res.sendfile('worldNews.json');
});

app.get('/politics.json', function (req, res) {
  res.sendfile('politics.json');
});

app.get('/science.json', function (req, res) {
  res.sendfile('science.json');
});

app.get('/technology.json', function (req, res) {
  res.sendfile('technology.json');
});


var port = process.env.PORT || 3000;
app.listen(port, function() {
  console.log('Server running at' + port);
});