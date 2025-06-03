def circle_calc(radius):
    return 3.14*radius*radius, 2*3.14*radius, 2*radius

circle_radius= int(input("Enter the radius of circle:- "))
area, circumference, diameter= circle_calc(circle_radius)

print(f"Area of circle is {area}\nCircumference of circle is {circumference}\nDiameter of circle is {diameter}")