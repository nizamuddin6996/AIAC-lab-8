def assign_grade(score):
    """
    Assigns a letter grade based on the numerical score.
    
    Args:
        score: A numerical score (int or float)
        
    Returns:
        str: Letter grade (A, B, C, D, or F)
        
    Raises:
        TypeError: If score is not a number
        ValueError: If score is not a valid number
    """
    # Check if input is a valid number
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    
    # Check if score is a valid number (not NaN or infinity)
    if score != score or score == float('inf') or score == float('-inf'):
        raise ValueError("Score must be a valid number")
    
    # Assign grade based on score ranges
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    try:
        score_input = input("Enter the score: ")
        score = float(score_input)
        print(assign_grade(score))
    except ValueError:
        print("Invalid input: score must be a number.")
    except TypeError as e:
        print(f"Type error: {e}")
