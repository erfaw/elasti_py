def calculate_love_score(name1, name2):
  llist = ['TRUE', 'LOVE']
  true_count = 0
  love_count = 0

  for y in 'TRUE':
      true_count += name1.upper().count(y)
      true_count += name2.upper().count(y)
  for y in 'LOVE':
      love_count += name1.upper().count(y)
      love_count += name2.upper().count(y)

  return print(f"{true_count}{love_count}")

name1 = input("name1: ")
name2 = input("name2: ")

calculate_love_score(name1, name2)

