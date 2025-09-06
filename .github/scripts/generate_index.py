import os

TOOLS_DIR = "tools"
INDEX_FILE = "index.html"

# 模板 HTML 上下文
HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>折纸工具合集</title>
<link rel="stylesheet" href="res/css/style.css">
<style>
body { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; background-color:#f0f0f0; color:#333; margin:0; padding:0; }
header { background-color:#222; color:#fff; padding:1rem; text-align:center; }
header p { color:#ccc; margin-top:0.3rem; }
main { max-width:1000px; margin:2rem auto; display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:1.5rem; padding:0 1rem; }
.tool-card { background-color:#fff; border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.1); padding:1rem; display:flex; flex-direction:column; transition:transform 0.2s, box-shadow 0.2s; }
.tool-card:hover { transform:translateY(-5px); box-shadow:0 4px 12px rgba(0,0,0,0.2); }
.tool-card h2 { margin:0 0 0.5rem 0; font-size:1.2rem; color:#111; }
.tool-card p { flex:1; font-size:0.95rem; color:#555; }
.tool-card a { margin-top:1rem; text-decoration:none; color:#fff; background-color:#333; padding:0.5rem; text-align:center; border-radius:5px; transition:background-color 0.2s; }
.tool-card a:hover { background-color:#555; }
footer { text-align:center; padding:1rem; font-size:0.9rem; color:#888; background-color:#f0f0f0; margin-top:2rem; }
</style>
</head>
<body>
<header>
<h1>折纸工具合集</h1>
<p>汇集各种折纸设计工具和资源</p>
</header>
<main>
"""

HTML_FOOTER = """
</main>
<footer>
&copy; 2025 折纸工具合集 | GitHub Pages
</footer>
</body>
</html>
"""

def get_tools():
    tools = []
    for tool_name in sorted(os.listdir(TOOLS_DIR)):
        tool_path = os.path.join(TOOLS_DIR, tool_name)
        if os.path.isdir(tool_path):
            # 尝试读取 README.md 第一行作为简介
            readme_file = os.path.join(tool_path, "README.md")
            desc = "暂无描述"
            if os.path.exists(readme_file):
                with open(readme_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            desc = line
                            break
            # index.html 链接
            link = f"{TOOLS_DIR}/{tool_name}/index.html"
            tools.append({"name": tool_name, "desc": desc, "link": link})
    return tools

def generate_index(tools):
    cards_html = ""
    for t in tools:
        cards_html += f"""<div class="tool-card">
<h2>{t['name']}</h2>
<p>{t['desc']}</p>
<a href="{t['link']}">前往工具</a>
</div>
"""
    return HTML_HEAD + cards_html + HTML_FOOTER

if __name__ == "__main__":
    tools = get_tools()
    html_content = generate_index(tools)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {INDEX_FILE} with {len(tools)} tools.")
