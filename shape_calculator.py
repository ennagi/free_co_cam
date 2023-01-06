 class Rectangle:
    def __init__(self,width=0.0,hight=0.0):
        self.width=width
        self.hight=hight


    def set_width(self,w):
        self.w=int(self.width)
        return self.w

    def set_height(self,h):
        self.h=int(self.hight)
        return self.h

    def get_area(self):
        return self.hight * self.width
        #print('the Area is : '+ format(self.hight * self.width)+' m2')

    def get_perimeter(self):
        print('the perimeter is: '+ format(2 * self.hight + 2 * self.width)+' m')

    def get_diagonal(self):
        
        print('the diagonale ist: '+ format((self.width **2 + self.hight**2)**0.5))

    def get_picture(self):
        for wi in range(self.hight ):
            for wi in range(self.width):
                if self.hight>50 or self.width>50:
                    print("Too big for picture.")
                    break
                print('*',end=' ')
            print()
          

    def get_amount_inside(self,c):
        return self.get_area() // c.get_area()

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.hight})'



class Square(Rectangle):
    def __init__(self, width=0, hight=0):
        super().__init__(self,width)
        self.width=width
        self.hight=width

    def set_side(self,seid):
        self.width=seid
        self.height=seid
        return seid

    

    def __repr__(self) :
        return f'Square(side={self.hight})'
