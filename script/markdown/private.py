import re

# 独立段落处理
def set_title(line):
    if line.startswith('##### '):
        html_lines = f'<h5>{line[6:]}</h5>'
    elif line.startswith('#### '):
        html_lines = f'<h4>{line[5:]}</h4>'
    elif line.startswith('### '):
        html_lines = f'<h3>{line[4:]}</h3>'
    elif line.startswith('## '):
        html_lines = f'<h2>{line[3:]}</h2>'
    elif line.startswith('# '):
        html_lines = f'<h1>{line[2:]}</h1>'
    else:
        return "", False
    return html_lines, True

# 图片转换
def set_image(line):
    pattern = r'^!\[(.*?)\]\((.*?)(?:\s+"(.*?)")?\)$'
    match = re.match(pattern, line.strip())
    if match:
        alt_text = match.group(1) or ''
        img_url = match.group(2)
        title = match.group(3)
        if title:
            return f'<img src="{img_url}" alt="{alt_text}" title="{title}">', True
        else:
            return f'<img src="{img_url}" alt="{alt_text}">', True
    else:
        return "", False


# 代码块处理
def set_blockquote(line):
    if line.startswith('> '):
        processed_line = process_inline_styles(line)
        html_lines = f'<blockquote>{processed_line[2:]}</blockquote>'
    else:
        return "", False
    return process_links(html_lines), True

# 普通段落
def set_pline(line):
    if line.strip() and line :
        processed_line = process_inline_styles(line)
        html_lines = f'<p>{processed_line}</p>'.replace("\t", "    ").replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;")
    else:
        return "", False
    return process_links(html_lines), True

# 处理行内样式：**粗体** 和 `行内代码`
def process_inline_styles(text):
    
    # 处理粗体 **text**
    def replace_bold(match):
        return f'<strong>{match.group(1)}</strong>'
    text = re.sub(r'\*\*(.*?)\*\*', replace_bold, text)
    
    # 处理行内代码 `code`
    def replace_code(match):
        return f'<code>{match.group(1)}</code>'
    text = re.sub(r'`(.*?)`', replace_code, text)
    
    return text

# 处理链接路径
def process_links(text):
    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)

        if not link_url.startswith(('http://', 'https://', '#', 'mailto:', 'tel:')):
            link_url = link_url.replace('.md', '.html')
        return f'<a href="{link_url}">{link_text}</a>'
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, replace_link, text)

# 处理表格方法
def parse_table(lines, start_ptr):
    table_rows = []
    ptr = start_ptr

    while ptr < len(lines) and '|' in lines[ptr]:
        table_rows.append(lines[ptr].strip())
        ptr += 1

    if len(table_rows) < 2:
        return "", start_ptr

    html = ['<table>']

    headers = [cell.strip() for cell in table_rows[0].split('|')[1:-1]]
    html.append('  <thead>')
    html.append('    <tr>')
    for header in headers:
        html.append(f'      <th>{header}</th>')
    html.append('    </tr>')
    html.append('  </thead>')

    alignments = []
    if len(table_rows) > 1 and set(table_rows[1].replace('|', '').replace(' ', '')).issubset({'-', ':'}):
        align_cells = table_rows[1].split('|')[1:-1]
        for cell in align_cells:
            cell = cell.strip()
            if cell.startswith(':') and cell.endswith(':'):
                alignments.append(' center')
            elif cell.endswith(':'):
                alignments.append(' right')
            elif cell.startswith(':'):
                alignments.append(' left')
            else:
                alignments.append('')
        start_data_row = 2
    else:
        start_data_row = 1
        alignments = [''] * len(headers)

    html.append('  <tbody>')
    for i in range(start_data_row, len(table_rows)):
        cells = [cell.strip() for cell in table_rows[i].split('|')[1:-1]]
        html.append('    <tr>')
        for j, cell in enumerate(cells):
            if j < len(alignments):
                align_class = f' style="text-align:{alignments[j].strip()};"' if alignments[j] else ''
                html.append(f'      <td{align_class}>{cell}</td>')
            else:
                html.append(f'      <td>{cell}</td>')
        html.append('    </tr>')
    html.append('  </tbody>')
    html.append('</table>')

    return '\n'.join(html), ptr


