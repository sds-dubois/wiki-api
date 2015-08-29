from wikiapi import WikiApi

def main(term):
	wiki = WikiApi()

	# print 'Old find for:',term
	# results = wiki.find(term)
	# print results,'\n'

	print 'Test find_titles for:',term
	results1 = wiki.find_titles(term)
	print(results1)

	title = results1[0]
	print '\nTest find_related_categories for:', title
	results2 = wiki.find_related_categories(title)
	print(results2)

	cat = results2[0]
	print '\nTest find_related_titles for:', cat
	results3 = wiki.find_related_titles(cat)
	print(results3)


if __name__ == "__main__":
	term = 'einstein'
	main(term)
