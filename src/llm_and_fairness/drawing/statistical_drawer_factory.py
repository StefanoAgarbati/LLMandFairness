from drawing.statistical_drawer_seaborn import StatisticalDrawerSeaborn


class StatisticalDrawerType:
    SEABORN = 'seaborn'


class StatisticalDrawerFactory:

    @staticmethod
    def create_statistical_drawer(name):
        match name:
            case StatisticalDrawerType.SEABORN:
                return StatisticalDrawerSeaborn()
            case _:
                raise Exception(f"StatisticalDrawerFactory -> the drawer {name} doesn't exist")