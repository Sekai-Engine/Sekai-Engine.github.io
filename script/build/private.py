import os
import shutil
import re
from pathlib import Path
import markdown.public as markdown

# 清理对应path的路径文件
def path_clear(OUT):
    if os.path.exists(OUT): 
        shutil.rmtree(OUT)
    
    os.makedirs(OUT, exist_ok=True)

# 复制`./static`静态资源
def static_copy(ROOT, OUT, static):
    shutil.copytree(os.path.join(ROOT, static), os.path.join(OUT, static), dirs_exist_ok=True)

# 导入模板{file_name: file_data}
def load_template(ROOT, templates):
    template_dict = {}
    for item in Path(os.path.join(ROOT, templates)).rglob('*'):
        with open(item) as f:
            template_dict[item.name] = f.read()
    return template_dict

# 添加组件文件
def load_files_path(ROOT, templates, components):
    template_dict = load_template(ROOT, templates)
    for template_name in template_dict:
        template = template_dict[template_name]
        for item in Path(os.path.join(ROOT, components)).rglob('*'):
            if item.is_file() and item.name[-5:] == ".html":
                if f"${{{item.name[:-5]}}}" in template:
                    with open(item) as f:
                        file_data = f.read()
                    template = template.replace(f"${{{item.name[:-5]}}}", file_data)
        template_dict[template_name] = template
    return template_dict

# 文件识别模板并写入
def set_template(ROOT, OUT, pages, templates, components, pages_name):
    template_dict = load_files_path(ROOT, templates, components)
    for item in Path(os.path.join(ROOT, pages)).rglob('*'):
        if item.is_file() and item.suffix in [".html", ".md"]:
            with open(item) as f:
                page_data = f.read()
            content = page_data.split('\n')[0].lstrip()
            match = re.match(r'<!--\s*(.*?)\s*-->', content, re.DOTALL)
            if match:
                template_name = match.group(1).strip()
                template = template_dict[template_name]
                if item.name[-3:] == ".md":
                    item = str(item)[:-3] + ".html"
                    page_data = markdown.md(page_data)
                template = template.replace(pages_name, page_data)
                out_path = OUT + str(item)[len(os.path.join(ROOT, pages)):]
                path = Path(out_path)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(template)
            else:
                print_log = "Error:./build/private.py set_template(): "
                print_log += "not found template.\n"
                print_log += f"\tfile path: {item}\n"
                print_log += f"\tfile content: {content}"
                print(print_log)
                continue
