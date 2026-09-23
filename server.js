require('dotenv').config();
const express = require('express');
const cors = require('cors');
const apiRouter = require('./src/routes/api');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
// Canonicalize /index.html -> / (must precede static)
app.get('/index.html', (req, res) => res.redirect(301, '/'));

app.use(express.static('public', { redirect: false }));

app.use('/api', apiRouter);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Canonicalize /index.html -> / to avoid duplicate content


app.listen(PORT, () => {
  console.log(`F13 LLC server running on http://localhost:${PORT}`);
});
