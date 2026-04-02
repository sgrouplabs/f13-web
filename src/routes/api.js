const express = require('express');
const router = express.Router();
const { submitQuote } = require('../db/supabaseClient');

// POST /api/quote — submit a new lead quote request
router.post('/quote', async (req, res) => {
  const { name, phone, email, service, details, zip } = req.body;

  if (!name || !phone || !email || !service || !zip) {
    return res.status(400).json({ error: 'Missing required fields: name, phone, email, service, zip' });
  }

  try {
    const lead = await submitQuote({ name, phone, email, service, details: details || '', zip });
    console.log('[API] POST /api/quote → lead created:', lead.id);
    res.status(201).json({ success: true, lead });
  } catch (err) {
    console.error('[API] POST /api/quote error:', err.message);
    res.status(500).json({ error: 'Failed to submit quote request. Please try again.' });
  }
});

module.exports = router;
