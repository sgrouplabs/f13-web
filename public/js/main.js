/* ─── F13 LLC — main.js ─────────────────────────────────── */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  initBeforeAfterSliders();
  initQuoteForm();
});

/* ─── 1. Sticky header shadow on scroll ─────────────────── */
function initStickyHeader() {
  const header = document.getElementById('site-header');
  if (!header) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ─── 2. Mobile menu toggle ─────────────────────────────── */
function initMobileMenu() {
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', () => {
    menu.classList.toggle('hidden');
    menu.classList.toggle('open');
    const icon = btn.querySelector('i');
    if (menu.classList.contains('open')) {
      icon.classList.remove('fa-bars');
      icon.classList.add('fa-xmark');
    } else {
      icon.classList.remove('fa-xmark');
      icon.classList.add('fa-bars');
    }
  });

  // Close menu when a link is clicked
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.add('hidden');
      menu.classList.remove('open');
      btn.querySelector('i').classList.remove('fa-xmark');
      btn.querySelector('i').classList.add('fa-bars');
    });
  });
}

/* ─── 3. Before / After Sliders ─────────────────────────── */
function initBeforeAfterSliders() {
  const sliders = document.querySelectorAll('.ba-slider');

  sliders.forEach(slider => {
    let isDragging = false;

    const move = (clientX) => {
      const rect = slider.getBoundingClientRect();
      const x = clientX - rect.left;
      const pct = Math.max(0, Math.min(100, (x / rect.width) * 100));
      const afterImg = slider.querySelector('.ba-after');
      const divider = slider.querySelector('.ba-divider');
      if (afterImg) afterImg.style.clipPath = `inset(0 0 0 ${pct}%)`;
      if (divider) divider.style.left = pct + '%';
    };

    slider.addEventListener('mousedown', (e) => {
      isDragging = true;
      move(e.clientX);
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      move(e.clientX);
    });

    window.addEventListener('mouseup', () => { isDragging = false; });

    // Touch support
    slider.addEventListener('touchstart', (e) => {
      isDragging = true;
      move(e.touches[0].clientX);
    }, { passive: true });

    slider.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      move(e.touches[0].clientX);
    }, { passive: true });

    slider.addEventListener('touchend', () => { isDragging = false; });
  });
}

/* ─── 4. Quote Form AJAX + Toast ─────────────────────────── */
function initQuoteForm() {
  const form = document.getElementById('quote-form');
  if (!form) return;

  const submitBtn = document.getElementById('submit-btn');
  const errorEl   = document.getElementById('form-error');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorEl.classList.add('hidden');

    // Gather fields
    const name    = form.name.value.trim();
    const phone   = form.phone.value.trim();
    const email   = form.email.value.trim();
    const service = form.service.value.trim();
    const details = form.details.value.trim();
    const zip     = form.zip.value.trim();

    // Client-side validation
    if (!name || !phone || !email || !service || !zip) {
      showError('Please fill in all required fields.');
      return;
    }
    if (!/^[0-9]{5}$/.test(zip)) {
      showError('ZIP code must be 5 digits.');
      return;
    }
    if (!/^\S+@\S+\.\S+$/.test(email)) {
      showError('Please enter a valid email address.');
      return;
    }

    // Disable button while submitting
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending…';

    try {
      const res = await fetch('/api/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, phone, email, service, details, zip })
      });

      const data = await res.json();

      if (res.ok) {
        showToast('Quote request sent! We\'ll call you shortly.', 'success');
        form.reset();
      } else {
        showToast((data && data.error) ? data.error : 'Something went wrong. Please try again.', 'error');
      }
    } catch (err) {
      console.error('[Form] submit error:', err);
      showToast('Connection error. Please check your internet and try again.', 'error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Quote Request';
    }
  });

  function showError(msg) {
    errorEl.textContent = msg;
    errorEl.classList.remove('hidden');
    errorEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

/* ─── 5. Toast Notification System ──────────────────────── */
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const icon = type === 'success'
    ? '<i class="fa-solid fa-circle-check toast-icon"></i>'
    : '<i class="fa-solid fa-triangle-exclamation toast-icon"></i>';

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `${icon}<span>${message}</span>`;
  container.appendChild(toast);

  // Remove after animation completes (4s total)
  setTimeout(() => {
    toast.remove();
  }, 4200);
}
