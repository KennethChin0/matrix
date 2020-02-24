from display import *
from draw import *
from matrix import *


m2 = new_matrix(0, 0)
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print("\nTesting ident. m1 =")
m1 = ident(1)
print_matrix(m1)
print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1, m2)
print_matrix(m2)
print("\nTesting Matrix mult. m1 =")
m1 = new_matrix(0, 0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)
print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1, m2)
print_matrix(m2)


screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix(0, 0)

add_edge(matrix,250,450,0,225,380,0)
add_edge(matrix,225,380,0,235,150,0)
add_edge(matrix,250,150,0,200,150,0)
add_edge(matrix,200,150,0,205,130,0)
add_edge(matrix,205,130,0,250,130,0)
add_edge(matrix,240,130,0,242,90,0)
add_edge(matrix,242,90,0,250,90,0)
# add_edge(matrix,250,450,0,250,200,0)

draw_lines( matrix, screen, color )

for point in matrix:
    point[0] = 500-point[0]
draw_lines( matrix, screen, color )


display(screen)
