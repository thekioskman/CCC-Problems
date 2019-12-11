#CCC '97 S1 - Sentences
cases = int(input())

for tests in range(cases):
  subjects = []
  verbs = []
  objects = []
  num_sub = int(input())
  num_verb = int(input())
  num_objects = int(input())

  for x in range(num_sub):
    line = input()
    subjects.append(line)

  for x in range(num_verb):
    line = input()
    verbs.append(line)

  for x in range(num_objects):
    line = input()
    objects.append(line)

  for s in subjects:
    for v in verbs:
      for o in objects:
        print(s+" "+v+" "+o+".")
