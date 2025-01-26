def count_sides(edges):
    # Sort edges by the first element (row), and then by the second element (column)
    edges.sort()

    sides = 0
    for i in range(1, len(edges)):
        # Compare adjacent edges and check if they form a valid side (same row and adjacent columns)
        if edges[i][0] == edges[i-1][0] and abs(edges[i][1] - edges[i-1][1]) == 1:
            sides += 1

    return sides

# Example usage
edges = [(-0.5, 0.0), (0.5, 0.0), (0.0, -0.5), (-0.5, 1.0), (0.5, 1.0), 
         (-0.5, 2.0), (0.5, 2.0), (-0.5, 3.0), (0.5, 3.0), (0.0, 3.5)]

print(count_sides(edges))  # Expected output: 4
