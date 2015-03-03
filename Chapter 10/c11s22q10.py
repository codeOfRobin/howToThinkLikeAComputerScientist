def replace(s,old,new):
	return new.join(s.split(old))
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print replace(s, "om", "am")