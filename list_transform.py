def list_transform(file_path):
    # Initialize an empty list to hold the 2D list
    result = []
    
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read the lines from the file
        lines = f.readlines()
        
        # Iterate over each line and split it by whitespace
        for line in lines:
            row = line.strip().split()
            
            
            # Add the row to the result list
            result.append(row)
    #delete empty rows
    result = list(filter(lambda x: len(x)!= 0, result))
    return result