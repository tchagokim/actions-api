import sys

action_name = sys.argv[1]

s = """class _fn_Actions:
    def __init__(self, data):
        self.data = data"""

with open(f"./actions/{action_name}.py","w") as f:
    f.write(s.replace("_fn_",action_name.capitalize()))

print("Action name:",action_name)

