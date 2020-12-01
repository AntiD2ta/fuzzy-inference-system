from src.membership import *
from src.defuzzification import *
from src.systems import Larsen, Mamdani
from src.var_factory import make_variable

import typer

def main(
    co2: int = typer.Argument(... ,help='Concentration of co2 in ppm. Use values between 300 and 1000'),
    irrigation: int = typer.Argument(..., help='Irrigation frequency in times per week. Use values between 0 and 16'), 
    seed_quality: int = typer.Argument(..., help='Quality of seed in germination percentage. Use values between 0 and 100'),
    method: str = typer.Option('Mamdani', help='Aggregation method. Available: Mamdani, Larsen'),
    defuzz = typer.Option('centroid', help='Defuzzification method to use. Available: centroid, bisection, lom, mom, som'),
    graph: bool = typer.Option(False, help='Set if you want to see the graphs of the memberships functions of the process')
    ):
    '''
    Run the example problem
    '''

    assert method == 'Mamdani' or method == 'Larsen', 'Invalid aggregation method selected'

    defuzz_methods = {
        'centroid': centroid_defuzzification,
        'bisection': bisection_defuzzification,
        'lom': lom_defuzzification,
        'mom': mom_defuzzification,
        'som': som_defuzzification
    }
    assert defuzz in defuzz_methods, 'Invalid defuzzification method inserted'
    defuzz_func = defuzz_methods[defuzz]
    
    Co2 = make_variable('CO2')
    Co2 += 'low', LMembership(300, 360), 5
    Co2 += 'normal', PiMembership(300, 350, 380, 430), 5
    Co2 += 'high', PiMembership(380, 450, 525, 620), 5
    Co2 += 'optimum', PiMembership(500, 600, 700, 800), 5
    Co2 += 'very high', GammaMembership(650, 1000), 5

    Irrigation = make_variable('Irrigation')
    Irrigation += 'very deficient', LMembership(0, 4), 1
    Irrigation += 'deficient', LambdaMembership(1, 4, 7), 1
    Irrigation += 'good', LambdaMembership(4, 7, 10), 1
    Irrigation += 'excessive', LambdaMembership(7, 10, 13), 1
    Irrigation += 'very excessive', LambdaMembership(10, 13, 16), 1

    Seed_quality = make_variable('Seed_quality')
    Seed_quality += 'very poor', ZMembership(0, 25), 1
    Seed_quality += 'poor', GaussianMembership(25, 25), 1
    Seed_quality += 'acceptable', GaussianMembership(50, 25), 1
    Seed_quality += 'good', GaussianMembership(75, 25), 1
    Seed_quality += 'rich', SMembership(75, 100), 1

    Performance = make_variable('Performance')
    Performance += 'very low', ZMembership(0, 25), 1
    Performance += 'low', GaussianMembership(25, 25), 1
    Performance += 'regular', GaussianMembership(50, 25), 1
    Performance += 'high', GaussianMembership(75, 25), 1
    Performance += 'very high', SMembership(75, 100), 1

    if graph:
        Co2.graph()
        Irrigation.graph()
        Seed_quality.graph()
        Performance.graph()

    mamdani = Mamdani()
    mamdani += (
        Co2.Is('optimum') & Irrigation.Is('good') & (Seed_quality.Is('rich') | Seed_quality.Is('good')),
        Performance.Is('very high')
    )
    mamdani += (
        Co2.Is('optimum') & Irrigation.Is('good'),
        Performance.Is('high')
    )
    mamdani += (
        Co2.Is('high') & Irrigation.Is('good'),
        Performance.Is('high')
    )
    mamdani += (
        Co2.Is('high') & Seed_quality.Is('good'),
        Performance.Is('high')
    )
    mamdani += (
        Co2.Is('normal') & Seed_quality.Is('acceptable'),
        Performance.Is('regular')
    )
    mamdani += (
        Co2.Is('normal') & Irrigation.Is('good'),
        Performance.Is('regular')
    )
    mamdani += (
        Co2.Is('normal') & Seed_quality.Is('good'),
        Performance.Is('regular')
    )
    mamdani += (
        Irrigation.Is('deficient') | Irrigation.Is('excessive'),
        Performance.Is('low')
    )
    mamdani += (
        Seed_quality.Is('poor') & Co2.Is('low'),
        Performance.Is('low')
    )
    mamdani += (
        Irrigation.Is('very deficient') | Irrigation.Is('very excessive'),
        Performance.Is('very low')
    )
    mamdani += (
        (Co2.Is('low') | Co2.Is('very high')) | (Seed_quality.Is('poor') | Seed_quality.Is('very poor')),
        Performance.Is('very low')
    )


    if method == 'Mamdani':
        result = mamdani.infer( defuzz_func, graph,
            CO2=co2,
            Irrigation=irrigation,
            Seed_quality=seed_quality
        )
    else:
        larsen = Larsen()
        larsen.rules = mamdani.rules

        result = larsen.infer( defuzz_func, graph,
            CO2=co2,
            Irrigation=irrigation,
            Seed_quality=seed_quality
        )

    typer.echo(f'Results vector: {result}')


if __name__ == "__main__":
    typer.run(main)
