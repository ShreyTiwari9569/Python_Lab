def filter_matrix(matrix):
    return list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))


# Function to square every element of the matrix
def square_matrix(matrix):
    return list(map(
        lambda row: list(map(lambda x: x * x, row)),
        matrix
    ))


# Function to sort a tuple based on the second element
def sort_tuple(data):
    return sorted(data, key=lambda x: x[1])


# Input matrix
matrix = [
    [5, -2, 8, -1],
    [3, 7, -4, 6],
    [-9, 2, 1, -5]
]

# Input tuple data
data = (
    ("A", 30),
    ("B", 10),
    ("C", 20),
    ("D", 40)
)

print("Original Matrix:")
print(matrix)

# Filtering negative values
filtered = filter_matrix(matrix)
print("\nMatrix after removing negative values:")
print(filtered)

# Transforming matrix by squaring elements
squared = square_matrix(filtered)
print("\nSquared Matrix:")
print(squared)

# Sorting tuple data
sorted_data = sort_tuple(data)
print("\nOriginal Tuple Data:")
print(data)

print("\nSorted Tuple Data:")
print(sorted_data)