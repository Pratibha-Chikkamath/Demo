def clock_angle(hour, minute):
    # Normalize the hour to 12-hour format
    hour = hour % 12

    # Calculate angles
    hour_angle = 30 * hour + 0.5 * minute
    minute_angle = 6 * minute

    # Find the difference
    angle = abs(hour_angle - minute_angle)

    # Always take the smaller angle
    angle = min(angle, 360 - angle)

    return angle

# Example usage:
h = int(input("Enter hours (0-23): "))
m = int(input("Enter minutes (0-59): "))

angle = clock_angle(h, m)
print(f"Angle between hour and minute hands is: {angle} degrees")
