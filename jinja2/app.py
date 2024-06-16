from jinja2 import Environment, FileSystemLoader

# Set up the environment and load templates from the current directory
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('template.html')

# Define the data to render into the template
data = {
    'title': 'Hello World Page',
    'heading': 'Hello, World!',
    'message': 'This is a message rendered using Jinja2.'
}

# Render the template with data
rendered_html = template.render(data)

# Print or save the rendered HTML
print(rendered_html)