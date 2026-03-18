import markdown.private as private

def md(file_data):
    html_lines = ""
    ptr = 0
    lines = file_data.split("\n")
    while ptr < len(lines):
        line = lines[ptr]

        # 处理代码块（```）
        if line.strip().startswith('```'):
            code_content = []
            ptr += 1
            while ptr < len(lines) and not lines[ptr].strip().startswith('```'):
                code_content.append(lines[ptr])
                ptr += 1
            code_html = '<pre><code>' + '\n'.join(code_content) + '</code></pre>'
            html_lines += code_html
            ptr += 1
            continue
        
        if '|' in line and ptr + 1 < len(lines) and set(lines[ptr + 1].strip()).issubset({'|', '-', ' ', ':'}):
            table_html, new_ptr = private.parse_table(lines, ptr)
            html_lines += table_html
            ptr = new_ptr
            continue

        html, e = private.set_image(line)
        if e:
            ptr += 1
            html_lines += html
            continue
        html, e = private.set_title(line)
        if e:
            ptr += 1
            html_lines += html
            continue
        html, e = private.set_blockquote(line)
        if e:
            ptr += 1
            html_lines += html
            continue
        html, e = private.set_pline(line)
        if e:
            ptr += 1
            html_lines += html
            continue

        ptr += 1
    return html_lines














