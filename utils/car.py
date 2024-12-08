class Car:
    def __init__(self, reg_no, make, model, color, year):
        self.reg_no = reg_no
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def to_dict(self):

        return {
            "reg_no": self.reg_no,
            "make": self.make,
            "model": self.model,
            "color": self.color,
            "year": self.year
        }
