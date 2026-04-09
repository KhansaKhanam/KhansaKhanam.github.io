from pathlib import Path
html = Path('output/khansa-complete-portfolio.html').read_text(encoding='utf-8')

# replace the playground with bg.png
html = html.replace('      <div class="playground">', '      <div class="playground" style="background: url(\'bg.png\') center/cover; background-size: cover; background-position: center;">')
html = html.replace('        <div class="orbit"></div>', '')
html = html.replace('        <div class="orbit two"></div>', '')
html = html.replace('        <div class="blob one"></div>', '')
html = html.replace('        <div class="blob two"></div>', '')
html = html.replace('        <div class="character"></div>', '')
html = html.replace('        <div class="caption-card">\\n          <strong>Your research world</strong>\\n          <p>This can become a lab, notebook, or data visualization that reflects your work.</p>\\n        </div>', '')

# enhance the motion background
motion_script = '''
<script>
  const playground = document.querySelector('.playground');
  if (playground) {
    playground.addEventListener('mousemove', (e) => {
      const rect = playground.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width;
      const y = (e.clientY - rect.top) / rect.height;
      playground.style.backgroundPosition = \\`calc(50% + \\${(x - 0.5) * 40}px) calc(50% + \\${(y - 0.5) * 40}px)\\`;
    });
    playground.addEventListener('mouseleave', () => {
      playground.style.backgroundPosition = 'center center';
    });
  }
</script>
'''
html = html.replace('</body>', motion_script + '\n</body>')

Path('output/khansa-portfolio-bg-motion.html').write_text(html, encoding='utf-8')
print('updated with bg.png motion')