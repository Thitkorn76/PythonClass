class Calculate_area:

    # Instance Methond
    def rectangle_area(self, w, h):
        return w * h
    
    @classmethod
    def triangle_area(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r
    
cal = Calculate_area()
cal_rec = cal.rectangle_area(4,5)
cal_tri = cal.triangle_area(4,5)
cal_circle = cal.circle_area(5)

print('Rectang Area =', cal_rec)
print('Triangle Area = ', cal_tri)
print('Circle Area =', cal_circle)

# print('Test triangle Area', Calculate_area.triangle_area(5,6))
# print('Test Circle Area', Calculate_area.circle_area(5))
# print('Test Rectangle Area', Calculate_area.Re(5,6))