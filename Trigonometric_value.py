import random
import math

def trigonometric_values():
  
    angle = random.uniform(0, 360)
    print(f"Randomly generated angle: {angle:.2f} degrees")

    angle_in_radians = math.radians(angle)

    sine = math.sin(angle_in_radians)
    cosine = math.cos(angle_in_radians)
    tangent = math.tan(angle_in_radians)

    print(f"sin({angle:.2f}) = {sine:.4f}")
    print(f"cos({angle:.2f}) = {cosine:.4f}")


    if abs(cosine) < 1e-10:
        print(f"tan({angle:.2f}) = Undefined (cosine is too close to zero)")
    else:
        print(f"tan({angle:.2f}) = {tangent:.4f}")


trigonometric_values()
