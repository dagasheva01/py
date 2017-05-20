def count_words(text):
	#google how to split text to words with multiple delimiters ' ', '-', '.' etc
	words = special_split()
	counter = {}
	#убрать местоимения, предлоги и другие лишные слова
	words = exclude_odd_words(words)
	for w in words:
		if w in counter:
			counter[w] = counter[w] + 1
		else:
			counter[w] = 1

	#google how to sort dictionary by value
	top_counter = get_top_10(counter)
	return top_counter
