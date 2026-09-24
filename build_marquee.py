import urllib.request
import re

USER_SKILLS = {
    'python', 'java', 'pytorch', 'sklearn', 'pandas', 'numpy', 'mysql', 'mongodb', 'firebase', 'html', 'css', 'js', 'git', 'github', 'vscode'
}

ROW1_KEYS = [
    'python', 'react', 'pytorch', 'ts', 'pandas', 'docker', 'java', 'nextjs', 
    'mysql', 'aws', 'html', 'kubernetes', 'vscode', 'redis', 'flutter', 'fastapi', 'tensorflow', 'vite'
]

ROW2_KEYS = [
    'js', 'nodejs', 'sklearn', 'gcp', 'numpy', 'cpp', 'mongodb', 'rust', 
    'css', 'postgres', 'firebase', 'tailwind', 'git', 'go', 'github', 'linux', 'graphql', 'figma'
]

all_keys = list(dict.fromkeys(ROW1_KEYS + ROW2_KEYS))
print(f"Total skills to assemble: {len(all_keys)}")

icons_svg = {}

# 1. Fetch from Devicons for pandas and numpy
for k, devicon_url in [
    ('pandas', 'https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg'),
    ('numpy', 'https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg')
]:
    try:
        req = urllib.request.Request(devicon_url, headers={'User-Agent': 'Mozilla/5.0'})
        raw = urllib.request.urlopen(req).read().decode('utf-8')
        # Extract viewbox or inner contents
        vb_match = re.search(r'viewBox="([^"]+)"', raw)
        vb = vb_match.group(1) if vb_match else "0 0 128 128"
        inner = re.sub(r'^<svg[^>]*>', '', raw, flags=re.DOTALL)
        inner = re.sub(r'</svg>\s*$', '', inner, flags=re.DOTALL).strip()
        # Wrap with standard 256x256 container
        icons_svg[k] = f'<svg viewBox="{vb}" width="180" height="180" x="38" y="38">{inner}</svg>'
        print(f"  ✓ {k} (from Devicon)")
    except Exception as e:
        print(f"  ✗ Failed for {k}: {e}")

# 2. Fetch from skillicons.dev for the rest
for k in all_keys:
    if k in icons_svg:
        continue
    try:
        url = f"https://skillicons.dev/icons?i={k}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        raw = urllib.request.urlopen(req).read().decode('utf-8')
        m = re.search(r'<svg[^>]*viewBox="0 0 256 256"[^>]*>.*?</svg>', raw, re.DOTALL)
        if not m:
            m = re.search(r'<svg[^>]*width="256"[^>]*>.*?</svg>', raw, re.DOTALL)
        if m:
            inner = m.group(0)
            inner_content = re.sub(r'^<svg[^>]*>', '', inner, flags=re.DOTALL)
            inner_content = re.sub(r'</svg>\s*$', '', inner_content, flags=re.DOTALL).strip()
            icons_svg[k] = inner_content
            print(f"  ✓ {k} (from SkillIcons)")
        else:
            print(f"  ✗ Regex failed for {k}")
    except Exception as e:
        print(f"  ✗ Error for {k}: {e}")

print(f"\nAll {len(icons_svg)} icons loaded successfully.")

# Layout Configuration
ICON_BOX_SIZE = 58
GAP = 14
ITEM_STEP = ICON_BOX_SIZE + GAP # 72px
SET1_COUNT = len(ROW1_KEYS) # 18
SET2_COUNT = len(ROW2_KEYS) # 18
SET1_WIDTH = SET1_COUNT * ITEM_STEP # 1296px
SET2_WIDTH = SET2_COUNT * ITEM_STEP # 1296px

VIEW_WIDTH = 890
VIEW_HEIGHT = 168

def make_unique_ids(svg_content, prefix):
    # Find all id="..." in the svg
    found_ids = set(re.findall(r'id=["\']([^"\']+)["\']', svg_content))
    out = svg_content
    for old_id in found_ids:
        new_id = f"{prefix}_{old_id}"
        out = re.sub(rf'id=["\']{re.escape(old_id)}["\']', f'id="{new_id}"', out)
        out = re.sub(rf'url\(#{re.escape(old_id)}\)', f'url(#{new_id})', out)
        out = re.sub(rf'href=["\']#{re.escape(old_id)}["\']', f'href="#{new_id}"', out)
    return out

def render_row_items(keys, row_id):
    items = []
    # 2 duplicate sets for smooth infinite loop
    double_keys = keys + keys
    for i, k in enumerate(double_keys):
        x = i * ITEM_STEP
        is_user = k in USER_SKILLS
        raw_content = icons_svg.get(k, '')
        
        # Scope internal IDs per item
        prefix = f"r{row_id}_i{i}_{k}"
        content = make_unique_ids(raw_content, prefix)
        
        # Scale 256x256 down to ICON_BOX_SIZE (58px)
        scale_factor = ICON_BOX_SIZE / 256.0 # 58 / 256 = 0.2265625
        
        if is_user:
            # Highlighted skill: 100% opacity, cyan cyberpunk neon glow & border, active badge dot
            card = f'''
        <g transform="translate({x}, 0)">
          <!-- Highlight Glow Backdrop -->
          <rect x="0" y="0" width="{ICON_BOX_SIZE}" height="{ICON_BOX_SIZE}" rx="14" fill="#151b28" stroke="#00F7FF" stroke-width="2" filter="url(#cyan-glow)" />
          <g transform="scale({scale_factor})">
            {content}
          </g>
          <rect x="0" y="0" width="{ICON_BOX_SIZE}" height="{ICON_BOX_SIZE}" rx="14" fill="none" stroke="#00F7FF" stroke-width="1.6" opacity="0.9" />
          <!-- Active Skill Indicator -->
          <circle cx="{ICON_BOX_SIZE - 7}" cy="7" r="3.5" fill="#00FF9D" stroke="#0d1117" stroke-width="1" />
        </g>'''
        else:
            # Dimmed skill: 28% opacity, subtle dark card, muted
            card = f'''
        <g transform="translate({x}, 0)" opacity="0.28" filter="url(#dim-grayscale)">
          <rect x="0" y="0" width="{ICON_BOX_SIZE}" height="{ICON_BOX_SIZE}" rx="14" fill="#0b0f17" stroke="#21262d" stroke-width="1" />
          <g transform="scale({scale_factor})">
            {content}
          </g>
        </g>'''
        items.append(card)
    return "\n".join(items)

row1_content = render_row_items(ROW1_KEYS, 1)
row2_content = render_row_items(ROW2_KEYS, 2)

svg_output = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEW_WIDTH} {VIEW_HEIGHT}" width="{VIEW_WIDTH}" height="{VIEW_HEIGHT}" fill="none">
  <defs>
    <!-- Cyan Neon Glow for Highlighted User Skills -->
    <filter id="cyan-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Grayscale / Dimming filter for other developer ecosystem skills -->
    <filter id="dim-grayscale">
      <feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 0.45 0"/>
    </filter>

    <!-- Edge Fading Gradients for Smooth Seamless Infinite Stream -->
    <linearGradient id="edge-fade-left" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#070a12" stop-opacity="1" />
      <stop offset="100%" stop-color="#070a12" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="edge-fade-right" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#070a12" stop-opacity="0" />
      <stop offset="100%" stop-color="#070a12" stop-opacity="1" />
    </linearGradient>

    <!-- Cyberpunk Border Gradient -->
    <linearGradient id="card-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F7FF" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#FF007F" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#00FF9D" stop-opacity="0.5" />
    </linearGradient>

    <style>
      @keyframes marquee-left {{
        0% {{ transform: translateX(0px); }}
        100% {{ transform: translateX(-{SET1_WIDTH}px); }}
      }}
      @keyframes marquee-right {{
        0% {{ transform: translateX(-{SET2_WIDTH}px); }}
        100% {{ transform: translateX(0px); }}
      }}
      .track-left {{
        animation: marquee-left 28s linear infinite;
      }}
      .track-right {{
        animation: marquee-right 28s linear infinite;
      }}
      .track-left:hover, .track-right:hover {{
        animation-play-state: paused;
      }}
    </style>
  </defs>

  <!-- Container Box -->
  <rect width="{VIEW_WIDTH}" height="{VIEW_HEIGHT}" rx="14" fill="#070a12" stroke="url(#card-border-grad)" stroke-width="1.5" />

  <!-- Marquee Rows -->
  <g transform="translate(12, 10)">
    <!-- Row 1: Moving Towards Left -->
    <g transform="translate(0, 8)">
      <g class="track-left">
{row1_content}
      </g>
    </g>

    <!-- Row 2: Moving Towards Right -->
    <g transform="translate(0, 80)">
      <g class="track-right">
{row2_content}
      </g>
    </g>
  </g>

  <!-- Left & Right Smooth Ribbon Edge Vignettes -->
  <rect x="0" y="0" width="85" height="{VIEW_HEIGHT}" rx="14" fill="url(#edge-fade-left)" pointer-events="none" />
  <rect x="{VIEW_WIDTH - 85}" y="0" width="85" height="{VIEW_HEIGHT}" rx="14" fill="url(#edge-fade-right)" pointer-events="none" />
</svg>
'''

with open("skills-marquee.svg", "w", encoding="utf-8") as f:
    f.write(svg_output)

print("Generated skills-marquee.svg successfully!")
