total_count = { "aluminum": 135, "plastic": 102, "paper": 213}

def sortItems(itemString):
  for letter in itemString:
    if letter == 'A':
      total_count["aluminum"] += 1
    elif letter == 'P':
      total_count["plastic"] += 1
    elif letter == 'R':
      total_count["paper"] += 1
  return total_count

sortItems('AAPAARRRRPAAPPRRP')
print(total_count)