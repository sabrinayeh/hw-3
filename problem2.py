"""
## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

### Skill you're practicing: Writing `while` loops.

Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

```
While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" and subtract 3 degrees from the temperature.

Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."
```

#### Starter Code

```python
temperature = 90
```

#### Expected Output

```
Temperature is 90 — crank the AC!
Temperature is 87 — crank the AC!
Temperature is 84 — crank the AC!
Temperature is 81 — crank the AC!
Temperature is 78 — crank the AC!
75. Ahh, that's better.
```

> **Hint:** Make sure that your loop conditional is being updated each iteration. Otherwise you'll end up with an infinite loop!
"""

temperature = 90
while temperature >= 75:
  if temperature == 75:
    print("75. Ahh, that's better.")
    break

  print("The temperature is", temperature, "-- crank the AC!")
  temperature -= 3
  