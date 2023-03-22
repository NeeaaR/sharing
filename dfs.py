network = {
    'sw1': ['sw2','sw3','sw4'],
    'sw2': ['sw5','sw6'],
    'sw3': ['sw1'],
    'sw4': ['sw1','sw7','sw8'],
    'sw5': ['sw9','sw10'],
    'sw6': ['sw2'],
    'sw7': ['sw4','sw11','sw12'],
    'sw8': ['sw4'],
    'sw9': ['sw5'],
    'sw10': ['sw5'],
    'sw11': ['sw7'],
    'sw12': ['sw7']
}
def find_path(network, start, end):

  stack = [(start, [start])]

  visited = set()

  while stack:

    (node, path) = stack.pop()

    if node not in visited:

      visited.add(node)

      if node == end:

        return path

      for neighbor in network[node]:
        
        stack.append((neighbor, path + [neighbor]))

  return None

print(find_path(network,'sw7','sw8'))