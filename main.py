from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

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

# draw_lines( matrix, screen, color )
display(screen)
