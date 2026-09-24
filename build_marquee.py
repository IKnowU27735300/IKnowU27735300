import urllib.request
import xml.etree.ElementTree as ET
import re

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

# User core skills & primary AI stack (Highlighted with Cyan Glow & 100% Opacity)
USER_SKILLS = {
    # Core Dev & ML
    'python', 'java', 'pytorch', 'sklearn', 'pandas', 'numpy', 'mysql', 'mongodb', 'firebase', 'supabase', 'html', 'css', 'js', 'git', 'github', 'vscode',
    # Primary AI & Agentic Stack
    'chatgpt', 'gemini', 'antigravity', 'cursor', 'windsurf', 'cline', 'notebooklm', 'lmstudio'
}

# Row 1 (23 items, scrolls LEFT)
ROW1_KEYS = [
    'python', 'chatgpt', 'react', 'gemini', 'pytorch', 'cursor', 
    'ts', 'antigravity', 'pandas', 'windsurf', 'docker', 'cline', 
    'java', 'trae', 'mysql', 'qwen', 'supabase', 'vscode', 'lmstudio', 
    'fastapi', 'codex', 'flutter', 'tensorflow'
]

# Row 2 (23 items, scrolls RIGHT)
ROW2_KEYS = [
    'js', 'notebooklm', 'nodejs', 'firebase', 'sklearn', 'z_ai', 
    'numpy', 'flow', 'mongodb', 'opencode', 'html', 'css', 
    'cpp', 'git', 'github', 'aws', 'gcp', 'postgres', 
    'tailwind', 'redis', 'kubernetes', 'sqlite', 'linux'
]

all_keys = list(dict.fromkeys(ROW1_KEYS + ROW2_KEYS))
print(f"Total skills & AI models to assemble: {len(all_keys)}")

icons_xml = {}

def make_svg_card(bg_color, inner_xml, width=256, height=256, rx=60):
    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <rect width="{width}" height="{height}" rx="{rx}" fill="{bg_color}"/>
  {inner_xml}
</svg>'''
    return ET.fromstring(svg_str)

# Custom Vector Cards for AI / LLM / Agentic Coding Tools
CUSTOM_AI_ICONS = {
    'chatgpt': make_svg_card('#10a37f', '''
      <g transform="translate(48, 48) scale(0.625)" fill="#FFFFFF">
        <path d="M220.5 137.5c-3.7-27.1-23.4-48.4-49.8-54.3-5.2-19.8-19.4-35.8-38.3-43.2-26.6-10.4-56.8-1.5-74.4 21.8-19.7-4.1-40.2 2.6-53.5 17.5-18.7 20.8-21.6 51.1-7.1 75-4.5 19.9-1.2 41 9.1 58.2 14.5 24.1 41.5 37.4 69.1 34 8.7 18.5 24.8 32.2 44.6 37.7 27.8 7.7 57.5-3.3 73.1-27.1 19.3 4.8 39.8-1.1 53.7-15.5 19.5-20.1 23.4-50.4 9.9-74.6 4.6-9.3 6.9-19.5 6.6-29.5zm-83.8 90.9c-11.4 0-22.3-4.3-30.7-12.1l1.8-1 51.2-29.6c2.7-1.6 4.4-4.5 4.4-7.6v-72.1l21.6 12.5c.3.2.5.5.5.8v61.4c0 26-21.2 47.7-48.8 47.7zm-93.5-44.5c-5.8-9.8-8.2-21.3-6.8-32.6l1.8 1.1 51.2 29.5c2.7 1.6 6 1.6 8.7 0l62.5-36.1v24.9c0 .4-.2.7-.4.9l-53.1 30.7c-22.5 13-51.5 6.3-63.9-18.4zm-14.7-93.4c5.5-10 14.7-17.5 25.6-21.1l-1.8 1.1v59.1c0 3.1 1.7 6 4.4 7.6l62.4 36-21.6 12.5c-.3.2-.7.2-1 0l-53.2-30.7c-22.5-13-30.2-41.5-14.8-64.5zm165.7 34.6l-62.4-36 21.6-12.5c.3-.2.7-.2 1 0l53.1 30.7c22.5 13 30.3 41.6 14.9 64.5-5.5 10-14.7 17.5-25.6 21.1l1.8-1.1v-59.1c0-3.1-1.7-6-4.4-7.6zm28.9-38.9c5.8 9.8 8.2 21.3 6.8 32.6l-1.8-1.1-51.2-29.5c-2.7-1.6-6-1.6-8.7 0l-62.5 36.1v-24.9c0-.4.2-.7.4-.9l53.1-30.7c22.6-13.1 51.5-6.4 63.9 18.4zm-94.8 5.7l27.5-15.9 27.5 15.9v31.7l-27.5 15.9-27.5-15.9v-31.7z"/>
      </g>'''),

    'gemini': make_svg_card('#131722', '''
      <defs>
        <linearGradient id="gemini_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#4E82EE"/>
          <stop offset="30%" stop-color="#7AA2F7"/>
          <stop offset="70%" stop-color="#BB9AF7"/>
          <stop offset="100%" stop-color="#F7768E"/>
        </linearGradient>
      </defs>
      <path d="M128 28C128 83.2285 172.771 128 228 128C172.771 128 128 172.771 128 228C128 172.771 83.2285 128 28 128C83.2285 128 128 83.2285 128 28Z" fill="url(#gemini_grad)"/>
      <circle cx="128" cy="128" r="14" fill="#FFFFFF" opacity="0.9"/>
    '''),

    'cursor': make_svg_card('#111318', '''
      <defs>
        <linearGradient id="cursor_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00F7FF"/>
          <stop offset="50%" stop-color="#7AA2F7"/>
          <stop offset="100%" stop-color="#FF007F"/>
        </linearGradient>
      </defs>
      <path d="M128 42L204 86V174L128 218L52 174V86L128 42Z" fill="#181c26" stroke="url(#cursor_grad)" stroke-width="6"/>
      <path d="M128 42L204 86L128 130L52 86L128 42Z" fill="#242b3d" opacity="0.8"/>
      <path d="M128 130V218L204 174V86L128 130Z" fill="#1e2333" opacity="0.9"/>
      <path d="M128 130V218L52 174V86L128 130Z" fill="#141824"/>
      <polygon points="128,95 155,130 135,130 135,160 121,160 121,130 101,130" fill="#00F7FF"/>
    '''),

    'windsurf': make_svg_card('#09141f', '''
      <defs>
        <linearGradient id="windsurf_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00F7FF"/>
          <stop offset="100%" stop-color="#00FF9D"/>
        </linearGradient>
      </defs>
      <path d="M60 185C95 185 125 150 145 110C165 70 185 55 205 55C190 90 170 135 140 165C110 195 75 200 50 195Z" fill="url(#windsurf_grad)"/>
      <path d="M45 145C80 145 110 115 130 80C148 48 168 38 185 38C170 68 150 105 125 130C98 155 65 160 45 145Z" fill="#00FF9D" opacity="0.6"/>
      <circle cx="165" cy="72" r="10" fill="#FFFFFF"/>
    '''),

    'cline': make_svg_card('#0f172a', '''
      <defs>
        <linearGradient id="cline_grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#00FF9D"/>
          <stop offset="100%" stop-color="#00F7FF"/>
        </linearGradient>
      </defs>
      <rect x="58" y="70" width="140" height="116" rx="36" fill="#1e293b" stroke="url(#cline_grad)" stroke-width="6"/>
      <rect x="76" y="96" width="104" height="42" rx="20" fill="#0f172a"/>
      <circle cx="102" cy="117" r="10" fill="#00FF9D"/>
      <circle cx="154" cy="117" r="10" fill="#00F7FF"/>
      <path d="M128 42V70M112 48H144" stroke="#00F7FF" stroke-width="6" stroke-linecap="round"/>
      <path d="M106 156C118 166 138 166 150 156" stroke="#00FF9D" stroke-width="5" stroke-linecap="round"/>
    '''),

    'antigravity': make_svg_card('#070913', '''
      <defs>
        <linearGradient id="anti_grad1" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00F7FF"/>
          <stop offset="100%" stop-color="#9B72CB"/>
        </linearGradient>
        <linearGradient id="anti_grad2" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#FF007F"/>
          <stop offset="100%" stop-color="#00FF9D"/>
        </linearGradient>
      </defs>
      <ellipse cx="128" cy="128" rx="84" ry="32" transform="rotate(-30 128 128)" stroke="url(#anti_grad1)" stroke-width="6" fill="none"/>
      <ellipse cx="128" cy="128" rx="84" ry="32" transform="rotate(30 128 128)" stroke="url(#anti_grad2)" stroke-width="6" fill="none"/>
      <ellipse cx="128" cy="128" rx="84" ry="32" transform="rotate(90 128 128)" stroke="#7AA2F7" stroke-width="3" stroke-dasharray="8 6" fill="none"/>
      <circle cx="128" cy="128" r="22" fill="#FFFFFF"/>
      <circle cx="128" cy="128" r="16" fill="#00F7FF"/>
      <circle cx="128" cy="128" r="8" fill="#FF007F"/>
    '''),

    'notebooklm': make_svg_card('#131a2a', '''
      <defs>
        <linearGradient id="nlm_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#8AB4F8"/>
          <stop offset="100%" stop-color="#C58AF9"/>
        </linearGradient>
      </defs>
      <rect x="62" y="52" width="112" height="152" rx="16" fill="#1a233a" stroke="url(#nlm_grad)" stroke-width="5"/>
      <path d="M62 52H84V204H62z" fill="#8AB4F8" opacity="0.4"/>
      <line x1="100" y1="90" x2="152" y2="90" stroke="#8AB4F8" stroke-width="5" stroke-linecap="round"/>
      <line x1="100" y1="116" x2="142" y2="116" stroke="#8AB4F8" stroke-width="5" stroke-linecap="round"/>
      <line x1="100" y1="142" x2="152" y2="142" stroke="#8AB4F8" stroke-width="5" stroke-linecap="round"/>
      <path d="M174 72C174 92 190 106 208 106C190 106 174 120 174 140C174 120 158 106 140 106C158 106 174 92 174 72Z" fill="url(#nlm_grad)"/>
    '''),

    'lmstudio': make_svg_card('#181028', '''
      <defs>
        <linearGradient id="lms_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#BB9AF7"/>
          <stop offset="100%" stop-color="#F7768E"/>
        </linearGradient>
      </defs>
      <rect x="64" y="64" width="128" height="128" rx="28" fill="#24183d" stroke="url(#lms_grad)" stroke-width="5"/>
      <polygon points="128,88 162,108 162,148 128,168 94,148 94,108" fill="#130c22" stroke="#BB9AF7" stroke-width="4"/>
      <circle cx="128" cy="128" r="14" fill="url(#lms_grad)"/>
      <line x1="128" y1="42" x2="128" y2="64" stroke="#F7768E" stroke-width="5" stroke-linecap="round"/>
      <line x1="128" y1="192" x2="128" y2="214" stroke="#F7768E" stroke-width="5" stroke-linecap="round"/>
      <line x1="42" y1="128" x2="64" y2="128" stroke="#BB9AF7" stroke-width="5" stroke-linecap="round"/>
      <line x1="192" y1="128" x2="214" y2="128" stroke="#BB9AF7" stroke-width="5" stroke-linecap="round"/>
    '''),

    'trae': make_svg_card('#0c1926', '''
      <defs>
        <linearGradient id="trae_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00F7FF"/>
          <stop offset="100%" stop-color="#00FF9D"/>
        </linearGradient>
      </defs>
      <path d="M56 68H200V104H146V198H110V104H56V68Z" fill="url(#trae_grad)"/>
      <polygon points="146,104 200,68 200,104" fill="#00FF9D" opacity="0.7"/>
      <polygon points="110,198 146,198 146,104" fill="#00F7FF" opacity="0.4"/>
    '''),

    'qwen': make_svg_card('#15112e', '''
      <defs>
        <linearGradient id="qwen_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#7C3AED"/>
          <stop offset="100%" stop-color="#3B82F6"/>
        </linearGradient>
      </defs>
      <polygon points="128,48 196,88 196,168 128,208 60,168 60,88" fill="none" stroke="url(#qwen_grad)" stroke-width="8"/>
      <circle cx="128" cy="48" r="12" fill="#3B82F6"/>
      <circle cx="196" cy="88" r="12" fill="#7C3AED"/>
      <circle cx="196" cy="168" r="12" fill="#3B82F6"/>
      <circle cx="128" cy="208" r="12" fill="#7C3AED"/>
      <circle cx="60" cy="168" r="12" fill="#3B82F6"/>
      <circle cx="60" cy="88" r="12" fill="#7C3AED"/>
      <circle cx="128" cy="128" r="24" fill="#FFFFFF"/>
    '''),

    'z_ai': make_svg_card('#0f1b29', '''
      <defs>
        <linearGradient id="z_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00F7FF"/>
          <stop offset="100%" stop-color="#3B82F6"/>
        </linearGradient>
      </defs>
      <path d="M62 66H194L114 150H194V190H62L142 106H62V66Z" fill="url(#z_grad)"/>
      <circle cx="194" cy="66" r="10" fill="#00FF9D"/>
      <circle cx="62" cy="190" r="10" fill="#00F7FF"/>
    '''),

    'codex': make_svg_card('#15171f', '''
      <defs>
        <linearGradient id="codex_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#10A37F"/>
          <stop offset="100%" stop-color="#00F7FF"/>
        </linearGradient>
      </defs>
      <path d="M92 86L48 128L92 170" stroke="url(#codex_grad)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <path d="M164 86L208 128L164 170" stroke="url(#codex_grad)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <line x1="142" y1="74" x2="114" y2="182" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/>
    '''),

    'opencode': make_svg_card('#121b24', '''
      <defs>
        <linearGradient id="open_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00FF9D"/>
          <stop offset="100%" stop-color="#7AA2F7"/>
        </linearGradient>
      </defs>
      <rect x="52" y="62" width="152" height="132" rx="24" fill="#182330" stroke="url(#open_grad)" stroke-width="6"/>
      <circle cx="78" cy="88" r="6" fill="#FF007F"/>
      <circle cx="98" cy="88" r="6" fill="#FFE052"/>
      <circle cx="118" cy="88" r="6" fill="#00FF9D"/>
      <path d="M82 132L108 152L82 172" stroke="#00FF9D" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <line x1="126" y1="172" x2="164" y2="172" stroke="#00F7FF" stroke-width="6" stroke-linecap="round"/>
    '''),

    'flow': make_svg_card('#0f172a', '''
      <defs>
        <linearGradient id="flow_grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#F59E0B"/>
          <stop offset="100%" stop-color="#EC4899"/>
        </linearGradient>
      </defs>
      <circle cx="80" cy="80" r="22" fill="#F59E0B"/>
      <circle cx="80" cy="176" r="22" fill="#EC4899"/>
      <circle cx="176" cy="128" r="26" fill="#3B82F6"/>
      <path d="M100 90L154 118" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
      <path d="M100 166L154 138" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
      <circle cx="176" cy="128" r="12" fill="#FFFFFF"/>
    ''')
}

icons_xml.update(CUSTOM_AI_ICONS)

# 1. Devicon for pandas and numpy
for k, devicon_url in [
    ('pandas', 'https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg'),
    ('numpy', 'https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg')
]:
    if k in icons_xml:
        continue
    try:
        req = urllib.request.Request(devicon_url, headers={'User-Agent': 'Mozilla/5.0'})
        raw = urllib.request.urlopen(req).read().decode('utf-8')
        raw = re.sub(r'xmlns="[^"]+"', '', raw)
        root = ET.fromstring(raw)
        vb = root.attrib.get('viewBox', '0 0 128 128')
        
        container = ET.Element('{http://www.w3.org/2000/svg}svg', {'width': '256', 'height': '256', 'viewBox': '0 0 256 256', 'fill': 'none'})
        ET.SubElement(container, '{http://www.w3.org/2000/svg}rect', {'width': '256', 'height': '256', 'rx': '60', 'fill': '#242938'})
        
        inner_svg = ET.SubElement(container, '{http://www.w3.org/2000/svg}svg', {'viewBox': vb, 'width': '180', 'height': '180', 'x': '38', 'y': '38'})
        for child in list(root):
            inner_svg.append(child)
            
        icons_xml[k] = container
        print(f"  ✓ {k} (from Devicon)")
    except Exception as e:
        print(f"  ✗ Failed for {k}: {e}")

# 2. Batch fetch remaining SkillIcons
remaining_needed = [k for k in all_keys if k not in icons_xml]
if remaining_needed:
    batch_url = f"https://skillicons.dev/icons?i={','.join(remaining_needed)}&perline=50"
    req = urllib.request.Request(batch_url, headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    root = ET.fromstring(raw)
    
    extracted = [elem for elem in root.iter('{http://www.w3.org/2000/svg}svg') if elem != root]
    for k, elem in zip(remaining_needed, extracted):
        icons_xml[k] = elem
        print(f"  ✓ {k} (from SkillIcons batch)")

print(f"\nAll {len(icons_xml)} / {len(all_keys)} icons ready.")

# Marquee sizing
ICON_BOX_SIZE = 58
GAP = 14
ITEM_STEP = ICON_BOX_SIZE + GAP # 72px
SET1_COUNT = len(ROW1_KEYS) # 23
SET2_COUNT = len(ROW2_KEYS) # 23
SET1_WIDTH = SET1_COUNT * ITEM_STEP # 1656px
SET2_WIDTH = SET2_COUNT * ITEM_STEP # 1656px

VIEW_WIDTH = 900
VIEW_HEIGHT = 168

def render_row_svg_elements(keys, row_id):
    row_g = ET.Element('{http://www.w3.org/2000/svg}g', {'class': f'track-{ "left" if row_id == 1 else "right" }'})
    double_keys = keys + keys
    
    for i, k in enumerate(double_keys):
        x = i * ITEM_STEP
        is_user = k in USER_SKILLS
        prefix = f"r{row_id}_i{i}_{k}"
        
        item_g = ET.SubElement(row_g, '{http://www.w3.org/2000/svg}g', {'transform': f'translate({x}, 0)'})
        
        if not is_user:
            item_g.attrib['opacity'] = '0.30'
            item_g.attrib['filter'] = 'url(#dim-grayscale)'
            ET.SubElement(item_g, '{http://www.w3.org/2000/svg}rect', {
                'x': '0', 'y': '0',
                'width': str(ICON_BOX_SIZE), 'height': str(ICON_BOX_SIZE),
                'rx': '14', 'fill': '#0b0f17', 'stroke': '#21262d', 'stroke-width': '1'
            })
        else:
            ET.SubElement(item_g, '{http://www.w3.org/2000/svg}rect', {
                'x': '0', 'y': '0',
                'width': str(ICON_BOX_SIZE), 'height': str(ICON_BOX_SIZE),
                'rx': '14', 'fill': '#151b28', 'stroke': '#00F7FF', 'stroke-width': '2',
                'filter': 'url(#cyan-glow)'
            })

        scale_factor = ICON_BOX_SIZE / 256.0
        icon_wrapper = ET.SubElement(item_g, '{http://www.w3.org/2000/svg}g', {'transform': f'scale({scale_factor})'})
        
        icon_tree = icons_xml.get(k)
        if icon_tree is not None:
            icon_str = ET.tostring(icon_tree, encoding='unicode')
            found_ids = set(re.findall(r'id=["\']([^"\']+)["\']', icon_str))
            for old_id in found_ids:
                new_id = f"{prefix}_{old_id}"
                icon_str = re.sub(rf'id=["\']{re.escape(old_id)}["\']', f'id="{new_id}"', icon_str)
                icon_str = re.sub(rf'url\(#{re.escape(old_id)}\)', f'url(#{new_id})', icon_str)
                icon_str = re.sub(rf'href=["\']#{re.escape(old_id)}["\']', f'href="#{new_id}"', icon_str)
            
            reparsed = ET.fromstring(icon_str)
            for child in list(reparsed):
                icon_wrapper.append(child)
                
        if is_user:
            ET.SubElement(item_g, '{http://www.w3.org/2000/svg}rect', {
                'x': '0', 'y': '0',
                'width': str(ICON_BOX_SIZE), 'height': str(ICON_BOX_SIZE),
                'rx': '14', 'fill': 'none', 'stroke': '#00F7FF', 'stroke-width': '1.6', 'opacity': '0.9'
            })
            ET.SubElement(item_g, '{http://www.w3.org/2000/svg}circle', {
                'cx': str(ICON_BOX_SIZE - 7), 'cy': '7', 'r': '3.5',
                'fill': '#00FF9D', 'stroke': '#0d1117', 'stroke-width': '1'
            })

    return row_g

# Assemble Full Root SVG
root_svg = ET.Element('{http://www.w3.org/2000/svg}svg', {
    'viewBox': f'0 0 {VIEW_WIDTH} {VIEW_HEIGHT}',
    'width': str(VIEW_WIDTH),
    'height': str(VIEW_HEIGHT),
    'fill': 'none'
})

# Defs
defs = ET.SubElement(root_svg, '{http://www.w3.org/2000/svg}defs')

# Cyan Glow Filter
filter_glow = ET.SubElement(defs, '{http://www.w3.org/2000/svg}filter', {
    'id': 'cyan-glow', 'x': '-20%', 'y': '-20%', 'width': '140%', 'height': '140%'
})
ET.SubElement(filter_glow, '{http://www.w3.org/2000/svg}feGaussianBlur', {'stdDeviation': '3', 'result': 'blur'})
ET.SubElement(filter_glow, '{http://www.w3.org/2000/svg}feComposite', {'in': 'SourceGraphic', 'in2': 'blur', 'operator': 'over'})

# Dim grayscale filter
filter_dim = ET.SubElement(defs, '{http://www.w3.org/2000/svg}filter', {'id': 'dim-grayscale'})
ET.SubElement(filter_dim, '{http://www.w3.org/2000/svg}feColorMatrix', {
    'type': 'matrix',
    'values': '0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 0.45 0'
})

# Edge fade gradients
grad_left = ET.SubElement(defs, '{http://www.w3.org/2000/svg}linearGradient', {'id': 'edge-fade-left', 'x1': '0%', 'y1': '0%', 'x2': '100%', 'y2': '0%'})
ET.SubElement(grad_left, '{http://www.w3.org/2000/svg}stop', {'offset': '0%', 'stop-color': '#070a12', 'stop-opacity': '1'})
ET.SubElement(grad_left, '{http://www.w3.org/2000/svg}stop', {'offset': '100%', 'stop-color': '#070a12', 'stop-opacity': '0'})

grad_right = ET.SubElement(defs, '{http://www.w3.org/2000/svg}linearGradient', {'id': 'edge-fade-right', 'x1': '0%', 'y1': '0%', 'x2': '100%', 'y2': '0%'})
ET.SubElement(grad_right, '{http://www.w3.org/2000/svg}stop', {'offset': '0%', 'stop-color': '#070a12', 'stop-opacity': '0'})
ET.SubElement(grad_right, '{http://www.w3.org/2000/svg}stop', {'offset': '100%', 'stop-color': '#070a12', 'stop-opacity': '1'})

# Card border gradient
grad_border = ET.SubElement(defs, '{http://www.w3.org/2000/svg}linearGradient', {'id': 'card-border-grad', 'x1': '0%', 'y1': '0%', 'x2': '100%', 'y2': '100%'})
ET.SubElement(grad_border, '{http://www.w3.org/2000/svg}stop', {'offset': '0%', 'stop-color': '#00F7FF', 'stop-opacity': '0.6'})
ET.SubElement(grad_border, '{http://www.w3.org/2000/svg}stop', {'offset': '50%', 'stop-color': '#FF007F', 'stop-opacity': '0.3'})
ET.SubElement(grad_border, '{http://www.w3.org/2000/svg}stop', {'offset': '100%', 'stop-color': '#00FF9D', 'stop-opacity': '0.5'})

# CSS Style for Animation
style = ET.SubElement(defs, '{http://www.w3.org/2000/svg}style')
style.text = f'''
  @keyframes marquee-left {{
    0% {{ transform: translateX(0px); }}
    100% {{ transform: translateX(-{SET1_WIDTH}px); }}
  }}
  @keyframes marquee-right {{
    0% {{ transform: translateX(-{SET2_WIDTH}px); }}
    100% {{ transform: translateX(0px); }}
  }}
  .track-left {{
    animation: marquee-left 34s linear infinite;
  }}
  .track-right {{
    animation: marquee-right 34s linear infinite;
  }}
  .track-left:hover, .track-right:hover {{
    animation-play-state: paused;
  }}
'''

# Base container rect
ET.SubElement(root_svg, '{http://www.w3.org/2000/svg}rect', {
    'width': str(VIEW_WIDTH), 'height': str(VIEW_HEIGHT),
    'rx': '14', 'fill': '#070a12', 'stroke': 'url(#card-border-grad)', 'stroke-width': '1.5'
})

# Rows Container
main_g = ET.SubElement(root_svg, '{http://www.w3.org/2000/svg}g', {'transform': 'translate(12, 10)'})

# Row 1 (Left)
row1_wrapper = ET.SubElement(main_g, '{http://www.w3.org/2000/svg}g', {'transform': 'translate(0, 8)'})
row1_wrapper.append(render_row_svg_elements(ROW1_KEYS, 1))

# Row 2 (Right)
row2_wrapper = ET.SubElement(main_g, '{http://www.w3.org/2000/svg}g', {'transform': 'translate(0, 80)'})
row2_wrapper.append(render_row_svg_elements(ROW2_KEYS, 2))

# Edge Fade overlays
ET.SubElement(root_svg, '{http://www.w3.org/2000/svg}rect', {
    'x': '0', 'y': '0', 'width': '85', 'height': str(VIEW_HEIGHT),
    'rx': '14', 'fill': 'url(#edge-fade-left)', 'pointer-events': 'none'
})
ET.SubElement(root_svg, '{http://www.w3.org/2000/svg}rect', {
    'x': str(VIEW_WIDTH - 85), 'y': '0', 'width': '85', 'height': str(VIEW_HEIGHT),
    'rx': '14', 'fill': 'url(#edge-fade-right)', 'pointer-events': 'none'
})

# Output XML
final_xml = ET.tostring(root_svg, encoding='utf-8', xml_declaration=True).decode('utf-8')
with open("skills-marquee.svg", "w", encoding="utf-8") as f:
    f.write(final_xml)

# Validate XML strictly
tree = ET.parse("skills-marquee.svg")
print(f"✅ Verified: skills-marquee.svg is 100% VALID XML with Supabase & MySQL included ({len(all_keys)} items)!")
