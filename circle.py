import math


def area(r):
	'''Принимает число r (радиус круга), возвращает площадь круга с таким радиусом.
		
		Параметры:
			r (float): десятичное вещественное число
		
		Возвращаемое значение:
			math.pi * r * r: площадь круга с радиусом r
	'''
			
    return math.pi * r * r
	

def perimeter(r):
	'''Принимает число r (радиус круга), возвращает периметр круга с таким радиусом.
		
		Параметры:
			r (float): десятичное вещественное число
		
		Возвращаемое значение:
			2 * math.pi * r: периметр круга с радиусом r
	'''
    return 2 * math.pi * r

