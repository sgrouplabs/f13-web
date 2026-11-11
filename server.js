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

// Canonicalize non-trailing-slash city/service pages -> trailing slash (301)
app.get(['/:seg(attic-flooring|fence-staining|concrete)/*', '/:seg(attic-flooring|fence-staining)'], (req, res, next) => {
  if (req.path.endsWith('/') || req.path.endsWith('/index.html')) return next();
  res.redirect(301, req.path + '/');
});

// Strip index.html inside directories -> canonical directory URL (301)
app.get('*', (req, res, next) => {
  if (req.path !== '/index.html' && req.path.endsWith('/index.html')) {
    return res.redirect(301, req.path.replace(/index\.html$/, ''));
  }
  next();
});

app.use(express.static('public', { redirect: false }));

app.use('/api', apiRouter);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Canonicalize /index.html -> / to avoid duplicate content


app.listen(PORT, () => {
  console.log(`F13 LLC server running on http://localhost:${PORT}`);
});
