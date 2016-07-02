

header = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<!-- This is an automatically generated file.\n     It will be read and overwritten.\n     DO NOT EDIT! -->\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>\n<DL><p>\n'
bookmark_header  = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'

def create_list(raw_list):
	list_of_bookmarks = [] #list of bookmark-folder pairs
	list_of_folders   = []
	previous_line     = ''

	for line in raw_list:
		stripped_line = line.lstrip()

		if stripped_line[:7] == '<DT><H3':
			start_index    = stripped_line[5:].find('>')
			end_index 	   = stripped_line[5:].find('<')
			list_of_folders.insert(0, stripped_line[5:][start_index + 1: end_index])
		# the last folder does not have a name
		elif previous_line == '</DL><p>':
			list_of_folders.insert(0, 'Unsorted')

		if stripped_line[:6] == '<DT><A':
			list_of_bookmarks.append((line, list_of_folders[0]))

		previous_line = line.strip()

	return list_of_bookmarks, list_of_folders

def test_header(first_line):
	return first_line == bookmark_header

def get_date(line):
	date_index = line[0].find('ADD_DATE="') + 10 #10 is the length of 'ADD_DATE="'
	return int(line[0][date_index: date_index + 10]) #10 is the standard date length