mealCost = float(raw_input())
tipPercent = float(raw_input())
taxPercent = float(raw_input())

totalCost = round(mealCost + (mealCost*(tipPercent/100)) + (mealCost*(taxPercent/100)))

print "The total meal cost is " + str(int(totalCost)) + " dollars."