@outputSchema("name_str:chararray")
def json_author(string):
	if len(string) == 1:
		return ''
	else:
		author_string = string.split('[')[2].split(']')[0]
		author_string = author_string.replace(", ", ",")
		author_string = author_string.replace(" ", "_")
		author_string = author_string.replace(",","")
		return " ".join(author_string.split())

@outputSchema("name_str:chararray")
def answer_str(string):
	return " ".join(string.split("_"))