import geometria

radio = 5
area_circulo = geometria.calcular_areas_Circulo(radio)
perimetro_circulo = geometria.calcular_area_perimetroCirculo(radio)

base = 4
altura = 6
area_rectangulo = geometria.calcular_area_rectangulo(base, altura)
perimetro_rectangulo = geometria.calcular_perimetro_rectangulo(base, altura)

base = 3
altura = 4
lado1 = 5
lado2 = 6
lado3 = 7
area_triangulo = geometria.calcular_area_triangulo(base, altura)
perimetro_triangulo = geometria.calcular_perimetro_triangulo(lado1, lado2, lado3)


print("Area y perimetro del circulo:")
print("Area:", area_circulo)
print("Perimetro", perimetro_circulo)
print()

print("Area y perimetro del rectangulo:")
print("Area:", area_rectangulo)
print("Perimetro", perimetro_rectangulo)
print()

print("Area y perimetro del trangulo:")
print("Area:", area_triangulo)
print("Perimetro", perimetro_triangulo)