fractal_tree = {
  'axiom': '0',
  'rules': {
    '1': '11',
    '0': '1[0]0'
  },
  'steps': 6,
  'commands': {
    '[': lambda t: (t.store(), t.left(45)),
    ']': lambda t: (t.restore(), t.right(45)),
    '1': lambda t: t.draw(10),
    '0': lambda t: t.draw(10)
  }
}

cantor_set = {
  'axiom': 'A',
  'rules': {
    'A': 'ABA',
    'B': 'BBB'
  },
  'steps': 4,
  'commands': {
    'A': lambda t: t.draw(5),
    'B': lambda t: t.move(5)
  }
}

koch = {
  'axiom': 'F',
  'rules': {
    'F': 'F+F-F-F+F',
  },
  'steps': 5,
  'commands': {
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90),
    'F': lambda t: t.draw(5)
  }
}

sierpinski_triangle = {
  'axiom': 'F-G-G',
  'rules': {
    'F': 'F-G+F+G-F',
    'G': 'GG'
  },
  'steps': 5,
  'commands': {
    '+': lambda t: t.right(120),
    '-': lambda t: t.left(120),
    'F': lambda t: t.draw(7),
    'G': lambda t: t.draw(7)
  }
}

sierpinski_arrowhead = {
  'axiom': 'A',
  'rules': {
    'A': 'B-A-B',
    'B': 'A+B+A'
  },
  'steps': 6,
  'commands': {
    '+': lambda t: t.right(60),
    '-': lambda t: t.left(60),
    'A': lambda t: t.draw(5),
    'B': lambda t: t.draw(5)
  }
}

dragon = {
  'axiom': 'X',
  'rules': {
    'X': 'X+YF+',
    'Y': '-FX-Y'
  },
  'steps': 10,
  'commands': {
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90),
    'F': lambda t: t.draw(10)
  }
}

fractal_plant = {
  'axiom': 'X',
  'rules': {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF'
  },
  'steps': 5,
  'commands': {
    '+': lambda t: t.right(25),
    '-': lambda t: t.left(25),
    'F': lambda t: t.draw(5),
    '[': lambda t: t.store(),
    ']': lambda t: t.restore()
  }
}

quadratic_koch_island = {
  'axiom': 'F-F-F-F',
  'rules': {
    'F': 'F-F+F+FF-F-F+F',
  },
  'steps': 3,
  'commands': {
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90),
    'F': lambda t: t.draw(5)
  }
}

peano = {
  'axiom': 'X',
  'rules': {
    'X': 'XFYFX+F+YFXFY-F-XFYFX',
    'Y': 'YFXFY-F-XFYFX+F+YFXFY'
  },
  'steps': 3,
  'commands': {
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90),
    'F': lambda t: t.draw(5)
  }
}

board = {
  'axiom': 'F+F+F+F',
  'rules': {
    'F': 'FF+F+F+F+FF'
  },
  'steps': 3,
  'commands': {
    '+': lambda t: t.right(90),
    '-': lambda t: t.left(90),
    'F': lambda t: t.draw(5)
  }
}
