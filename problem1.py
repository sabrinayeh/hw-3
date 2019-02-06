"""
## Problem 1: IOU!

### Skill you're practicing: Writing `for` loops to iterate over a list.

You have a list of Disney characters and you want to find out if each of them contain `i`, `o`, or `u` in their names. Loop through each character in the list and print out the following:

```
If the name contains a "u," print out the name plus "U are so Uniquely U!"
Otherwise if the name contains an "i," print out the name plus "I bet you're Impressively Intelligent!"
Otherwise if the name contains an "o," print out the name plus "O My! How Original!"
Otherwise, print the name plus "Ehh, a's and e's are so ordinary."
```

#### Starter Code

```python
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]

```

#### Expected Output

```
simba I bet you're Impressively Intelligent!
ariel I bet you're Impressively Intelligent!
pumba U are so Uniquely U!
flounder U are so Uniquely U!
nala Ehh, a's and e's are so ordinary.
ursula U are so Uniquely U!
scar Ehh, a's and e's are so ordinary.
flotsam O My! How Original!
timon I bet you're Impressively Intelligent!
```


> **Hint**: You can determine whether or not a string contains a particular character with an `if` statement. For example, `if "b" in my_string:` will be true if `my_string` contains any b's.
"""




disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
for each_character in disney_characters:
	if "u" in each_character:
		print(each_character + ", U are so Uniquely U!")
	elif "i" in each_character:
		print(each_character + ", I bet you're Impressively Intelligent!")
	elif "o" in each_character:
		print(each_character + ", O My! How Original!")
	else:
		print(each_character + ", Ehh, a's and e's are so ordinary.")
