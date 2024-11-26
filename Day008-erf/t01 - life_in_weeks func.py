def life_in_weeks(age):
  weeks_of_life = age * 12 * 4
  ninety_week = 90 * 12 * 4
  print(f"You have {ninety_week - weeks_of_life} weeks left.")

life_in_weeks(int(input("tell us your age")))