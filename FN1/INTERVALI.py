def presjecanje(interval1, interval2):
  a, b = interval1
  c, d = interval2
  if a == c or a == d or b == c or b == d:
    return "Presjek je jedna tocka"
  if (a > d) or (c > b):
    return "Presjek je prazan skup"
  start = max(a, c)
  end = min(b, d)
  return (start, end)

interval1 = (1, 5)
interval2 = (4, 8)

intersekcija = presjecanje(interval1, interval2)

print(intersekcija)
