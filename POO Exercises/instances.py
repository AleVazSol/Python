class Coordenate:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distance(self, other_coordenate):
        x_diff = (self.x - other_coordenate.x)**2
        y_diff = (self.y - other_coordenate.y)**2

        return (x_diff + y_diff)**0.5


def run():
    coord_1 = Coordenate(3,30)
    coord_2 = Coordenate(4,8)

    print(coord_1.distance(coord_2))


if __name__ == "__main__":
    run();