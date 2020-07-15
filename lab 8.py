class Goods:
  def __init__(self, p,m,y):
    self.price=p
    self.model=m
    self.year=y
  def get_price(self):
    return self.price
  def get_model(self):
    return self.model
  def get_year(self):
    return self.year
  def set_price(self,p):
    self.price=p
  def set_model(self,m):
    self.model=m
  def set_year(self,y):
    self.year=y

class TV(Goods):
  def set_screen_diagonal(self, d):
    self.screen_diagonal=d
  def set_matrix_type(self, m):
    self.matrix_type=m
  def get_screen_diagonal(self):
    return self.screen_diagonal
  def get_matrix_type(self):
    return self.matrix_type
  def __str__(self):
    return "Телевізор:\nЦіна: "+str(self.price)+" грн.\nМодель: "+self.model+".\nРік випуску: "+str(self.year)+".\nДіагональ екрана: "+str(self.screen_diagonal)+".\nТип матриці: "+self.matrix_type+"."

class Phone(Goods):
  def set_operating_system(self, os):
    self.operating_system=os
  def set_count_camera(self, c):
    self.count_camera=c
  def get_operating_system(self):
    return self.operating_system
  def get_count_camera(self):
    return self.count_camera
  def __str__(self):
    return "Телефон:\nЦіна: "+str(self.price)+" грн.\nМодель: "+self.model+".\nРік випуску: "+str(self.year)+".\nОпераційна система: "+str(self.operating_system)+".\nКількість камер: "+str(self.count_camera)+"."

class Laptop(Goods):
  def set_screen_diagonal(self, d):
    self.screen_diagonal=d
  def set_processor_type(self, p):
    self.processor_type=p
  def get_screen_diagonal(self):
    return self.screen_diagonal
  def get_processor_type(self):
    return self.processor_type
  def __str__(self):
    return "Ноутбук:\nЦіна: "+str(self.price)+" грн.\nМодель: "+self.model+".\nРік випуску: "+str(self.year)+".\nДіагональ екрана: "+str(self.screen_diagonal)+".\nТип процесора: "+self.processor_type+"."

tv1=TV(5499,"first",2019)
tv1.set_screen_diagonal(42.6)
tv1.set_matrix_type("TFT-TN")
print(tv1)

print()

phone1=Phone(3599,"Second",2020)
phone1.set_operating_system("Android")
phone1.set_count_camera(4)
print(phone1)

print()

laptop1=Laptop(8999,"Third",2018)
laptop1.set_screen_diagonal(15.6)
laptop1.set_processor_type("CPU")
print(laptop1)
  