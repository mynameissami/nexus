def sum_calibration_values(document):
    total = 0
    for line in document.split('\n'):
        if line:
            first_digit = line[0] if line[0].isdigit() else ''
            last_digit = line[-1] if line[-1].isdigit() else ''
            if first_digit and last_digit:
                total += int(first_digit + last_digit)
    return total

# Example usage
document = open('mytxt.txt', 'r').read()
print(sum_calibration_values(document))