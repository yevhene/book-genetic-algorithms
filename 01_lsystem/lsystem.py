from types import LambdaType

class LSystem:
  def __init__(self, config):
    self.axiom = config['axiom']
    self.rules = config['rules']
    self.steps = config['steps']
    self.commands = config['commands']

  def generate(self):
    def unwrap(c):
      if c in self.rules and isinstance(self.rules[c], str):
        return self.rules[c]
      else:
        return c

    script = self.axiom
    for step in range(self.steps):
      script = ''.join([unwrap(c) for c in script])

    return script

  def execute(self, script, executor):
    for c in script:
      if c in self.commands:
        command = self.commands[c]
        if isinstance(command, LambdaType):
          command(executor)

  def run(self, executor):
    script = self.generate()
    self.execute(script, executor)
