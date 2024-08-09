from jinja2 import Environment, FileSystemLoader

template_dir = './messages'  # Directory containing your template files
env = Environment(loader=FileSystemLoader(template_dir))
template_name = 'test.json.j2'  # Replace with your template file name
template = env.get_template(template_name)
context = {'name': 'World'}
message = template.render(context)