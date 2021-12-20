# DZ ==== 20.12.21

class Temp:
    count = 0

    def cheeck_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    @staticmethod
    def far_in_cel(x):
        if Temp.cheeck_value(x):
            Temp.count += 1
            return (x - 32) * 5 / 9
        else:
            raise ValueError("Неверный формат данных")

    @staticmethod
    def cel_in_far(x):
        if Temp.cheeck_value(x):
            Temp.count += 1
            return (x * 9/5) + 32
        else:
            raise ValueError("Неверный формат данных")

    @staticmethod
    def col_zap():
        return Temp.count


t1 = Temp
print(t1.far_in_cel(68))
print(t1.cel_in_far(0))
print(t1.col_zap())