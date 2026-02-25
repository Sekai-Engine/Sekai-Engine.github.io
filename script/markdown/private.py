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

def set_blockquote(line):
    if line.startswith('> '):
        processed_line = process_inline_styles(line)
        html_lines = f'<blockquote>{processed_line[2:]}</blockquote>'
    else:
        return "", False
    return process_links(html_lines), True

def set_pline(line):
    if line.strip() and line :
        processed_line = process_inline_styles(line)
        html_lines = f'<p>{processed_line}</p>'
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


