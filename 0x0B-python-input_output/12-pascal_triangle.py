#!/usr/bin/python3
"""defining function"""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle."""
    if n <= 0:
        return []

    triangles = [[1]]  # Initialize with the first row

    while len(triangles) < n:
        tri = triangles[-1]  # Get the last row
        tmp = [1]  # Initialize the new row with 1
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])  # Calculate the values for the new row
        tmp.append(1)  # Add the last 1
        triangles.append(tmp)  # Append the new row to the triangle

    return triangles

# Example usage:
triangle = pascal_triangle(5)
for row in triangle:
    print(row)
