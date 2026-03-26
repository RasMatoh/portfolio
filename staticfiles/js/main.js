// ─── MOBILE MENU ───────────────────────────────
function toggleMenu() {
  document.getElementById('mobileMenu').classList.toggle('open');
}

// ─── NAV SHRINK ON SCROLL ──────────────────────
window.addEventListener('scroll', () => {
  const nav = document.getElementById('navbar');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 50);
});

// ─── FADE-UP ON SCROLL ─────────────────────────
const observer = new IntersectionObserver(entries => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('visible'), i * 80);
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ─── ACTIVE NAV LINK ───────────────────────────
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.href === window.location.href) link.classList.add('active');
});