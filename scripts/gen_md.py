import os

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
umtk_path = os.path.join(rootdir, 'umtk')
docs_path = os.path.join(rootdir, 'docs')

for root, dirs, files in os.walk(umtk_path):
    for file in files:
        if file.startswith('__'):
            continue
        file_path = os.path.join(root, file)
        if "image_res" in file_path or "static_res" in file_path:
            continue
        if file.endswith('.md'):
            md_path = file_path
            md_relpath = md_path.split("umtk")[-1].strip("/")
            dd = len(md_relpath.split('/')) + 1
            docs_md_path = os.path.join(docs_path, "umtk", md_relpath)
            os.makedirs(os.path.dirname(docs_md_path), exist_ok=True)
            with open(docs_md_path, "w") as md_file:
                md_file.write(f'<!--@include: {"../" * dd}umtk/{md_relpath}-->')
        if file.endswith('.py'):
            py_path = file_path
            py_relpath = py_path.split("umtk")[-1].strip("/")
            dd = len(py_relpath.split('/')) + 1
            docs_py_path = os.path.join(docs_path, "umtk", py_relpath).replace(".py", ".md")
            os.makedirs(os.path.dirname(docs_py_path), exist_ok=True)
            with open(docs_py_path, "w") as py_file:
                py_file.write('```python\n')
                py_file.write(f'<!--@include: {"../" * dd}umtk/{py_relpath}-->\n')
                py_file.write('```\n')
