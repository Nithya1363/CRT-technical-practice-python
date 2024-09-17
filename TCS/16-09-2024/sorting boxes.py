def calculate_min_effort(N, k, weights):
    # Find the index of the heaviest box
    max_weight = max(weights)
    max_index = weights.index(max_weight)
    
    # Move the heaviest box to the position k
    effort = 0
    
    # Sort the rest of the boxes except the heaviest
    sorted_weights = sorted(weights[:max_index] + weights[max_index+1:])
    
    # Calculate effort for the heaviest box to move to the position k
    if k-1 != max_index:  # If the heaviest is not already in position
        effort += max_weight * weights[k-1]
    
    # Insert the heaviest box back at the required position in the sorted list
    sorted_weights.insert(k-1, max_weight)
    
    # Calculate the effort to sort the remaining boxes
    for i in range(N):
        if weights[i] != sorted_weights[i]:
            effort += weights[i] * sorted_weights[i]
    
    return effort

# Input parsing
def main():
    # Read the number of boxes (N) and the position of the Head Post Master's office (k)
    N, k = map(int, input().split())
    
    # Read the weights of the boxes
    weights = list(map(int, input().split()))
    
    # If input is invalid, return
    if len(weights) != N or N <= 1:
        print("Invalid input")
        return
    
    # Calculate and print the minimum effort
    result = calculate_min_effort(N, k, weights)
    print(result)

# Run the program
if __name__ == "__main__":
    main()
