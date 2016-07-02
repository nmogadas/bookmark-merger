
import io
from bookmark_helper import *

first_file_name = input('Enter first file name, including extension: ')
second_file_name = input('Enter second file name, including extension: ')

first_file  = open(first_file_name, 'r') 
second_file = open(second_file_name, 'r')

first_file_header  = first_file.readline()
second_file_header = second_file.readline()

if not test_header(first_file_header) or not test_header(second_file_header):
	print('Files are not bookmark files')
	exit()

f_list = list(first_file)
s_list = list(second_file)

first_file.close()
second_file.close()

first_bookmarks, first_folders   = create_list(f_list)
second_bookmarks, second_folders = create_list(s_list)

first_bookmarks.extend(second_bookmarks)
first_folders.extend(second_folders)

bookmark_set = set(first_bookmarks)
folder_set   = set(first_folders)

ordered_bookmark_list = sorted(bookmark_set, key=get_date)   

# # break bookmark_set into its separate folders
# # then rejoin them using .extend(), with the folder name inbetween,
# # then join all elements with ''.join(list) and create a new html file

separated_by_folders = []

##### maybe move unsorted to last in folder_set
for folder in folder_set:
	separated_by_folders.append('    <DT><H3>' + folder + '</H3>\n')
	separated_by_folders.extend([x[0] for x in ordered_bookmark_list if x[1] == folder])

new_file = open('merged_bookmarks.html', 'w')
new_file.write(header)

for line in separated_by_folders:
	new_file.write(line)

new_file.close()
exit()

