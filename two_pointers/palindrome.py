text = "This is_America"
text = text.lower()

alnumText = "".join(c for c in text if c.isalnum())
print(alnumText)