import importlib
import inspect
import os

# Get the names of the files in the "hosts" directory
filenames = os.listdir("hosts")

# Get only the names of the files that end with ".py"
# to keep only the modules
module_filenames = [filename for filename in filenames if filename.endswith(".py") and not filename.startswith("_")]

# Load the modules from their names
# and reload the modules with importlib.reload()
modules = []
for filename in module_filenames:
    module_name = filename[:-3]  # Remove the ".py" extension from the file name
    module = importlib.import_module('hosts.' + module_name)
    importlib.reload(module)

    if module_name == "default":
        modules.insert(0, module)
    else:
        modules.append(module)

# Get all the classes in the loaded modules
classes = []
for module in modules:
    # Get all the members (attributes and functions) in the module
    members = inspect.getmembers(module)

    # Get only the members that are classes
    # using the isclass() function from inspect
    class_members = [member for member in members if inspect.isclass(member[1])]

    # Add the classes to the classes list
    classes.extend(class_members)

# Add all the classes to the addons variable
addons = [cls[1]() for cls in classes]