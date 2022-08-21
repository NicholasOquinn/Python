row_length = float(input('enter length of row'))
end_post = float(input('enter space used by end post assembly'))
vine_space = float(input('enter space between vines'))
num_grapevines = row_length - 2 * end_post / vine_space
print('the number of grapevines that can fit in a row are', num_grapevines)
