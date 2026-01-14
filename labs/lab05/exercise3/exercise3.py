
def find_bottleneck_index(traceroute):
    hop_index = 0
    largest_jump=0
    for i in range(1, len(traceroute)):
        if traceroute[i][1] - traceroute[i-1][1] > largest_jump:
           largest_jump = traceroute[i][1] - traceroute[i-1][1]
           hop_index = i -1
    return hop_index

# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
