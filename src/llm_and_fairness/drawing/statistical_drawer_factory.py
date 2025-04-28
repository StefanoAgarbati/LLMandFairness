from drawing.statistical_drawer_seaborn import StatisticalDistributionDrawerSeaborn


class StatisticalDrawerType:
    SEABORN = 'seaborn'


class StatisticalDrawerFactory:

    def create_statistical_drawer(self, name):
        match name:
            case StatisticalDrawerType.SEABORN:
                return StatisticalDistributionDrawerSeaborn
            case _:
                raise Exception(f"StatisticalDrawerFactory -> the drawer {name} doesn't exist")