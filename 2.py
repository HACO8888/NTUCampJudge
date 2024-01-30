def draw_triangle(N):
    if N == 0:
        return ""

    triangle = []
    for i in range(N):
        line = "_" * (N - i - 1) + "+" * (i + 1)
        triangle.append(line)

    return "\n".join(triangle)


input_numbers = []
while True:
    N = int(input(""))
    if N == 0:
        break

    input_numbers.append(N)

triangles = []
for N in input_numbers:
    triangle = draw_triangle(N)
    triangles.append(triangle)

output = "\n\n".join(triangles)
print(output)
