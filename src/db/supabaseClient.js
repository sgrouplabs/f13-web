const { createClient } = require('@supabase/supabase-js');

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.warn('[Supabase] Missing env vars — quotes will be logged only (Supabase not connected)');
}

const supabase = supabaseUrl && supabaseKey
  ? createClient(supabaseUrl, supabaseKey)
  : null;

/**
 * Inserts a new lead quote into the Supabase `leads` table.
 * Table schema:
 *   id          — uuid (auto)
 *   name        — text
 *   phone       — text
 *   email       — text
 *   service     — text
 *   details     — text
 *   zip         — text
 *   status      — text (default: 'new')
 *   created_at  — timestamptz (auto)
 */
async function submitQuote({ name, phone, email, service, details, zip }) {
  const payload = { name, phone, email, service, details, zip, status: 'new' };

  if (!supabase) {
    console.log('[Supabase stub] Would insert quote:', payload);
    return { id: 'stub-' + Date.now(), ...payload };
  }

  const { data, error } = await supabase
    .from('leads')
    .insert([payload])
    .select()
    .single();

  if (error) throw new Error(error.message);
  return data;
}

module.exports = { submitQuote };
