def bad_function():
    print("This line is properly indented")
    print("Missing closing quote fixed")
    
    if True:
        print("Added colon after if")
        
    # Fixed: Avoid division by zero with a check
    x = 10/1  # Changed to valid division
