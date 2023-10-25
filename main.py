import math
class Triangle:
    def exsist(self,side1,side2,side3):
        if side1<side2+side3 and side2<side1+side3 and side3<side2+side1:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")

    def area(self,side1,side2,side3):
        p=(side1+side2+side3)/2
        S=math.sqrt(p*(p-side1)*(p-side2)*(p-side3))
        print ("Площадь равна = ", S)

    def perimeter(self,side1,side2,side3):
        print("Периметр равен = =", side1+side2+side3)
print("Введите стороны треугольника")
while True:
    try:
        a=float(input("Сторона 1: "))
        b=float(input("Сторона 2: "))
        c=float(input("Сторона 3: "))
        break
    except ValueError:
        print("Введите корректное значение")

triangle=Triangle()
triangle.exsist(a,b,c)
triangle.area(a,b,c)
triangle.perimeter(a,b,c)