from requirements import parse

# Parse the requirements file
requirements = parse('requirements.txt')

# Extract the dependency names from the parsed requirements
dependencies = [str(req.req) for req in requirements]

print(dependencies)