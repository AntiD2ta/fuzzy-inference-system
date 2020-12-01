# Fuzzy Infetence System

An implementation of a Inference System using fuzzy logic for Simulation class.

## Starting

To use the project, clone it or download it to your local computer.

### Requirements 📋

This project was developed using  `python v-3.7.2`

To install the `python` dependencies simply open the console from the root location of the project and execute:

```bash
pip install -r requirements.txt
```

### Configure and run 🔧

To run the project execute:

```bash
python main.py <args>
```

If you want to know how to pass the required arguments, use the available options and thereby configurate the simulation, run the main script with the args listed by:

```bash
python main.py --help
```

The program will offers you instructions. Here a example of interactive simulation at the start and end of a simulation:

## Usage ⚙️

To create linguistic variables use:

```python

var = make_variable('var')
var += 'low', LMembership(300, 360)
var += 'normal', PiMembership(300, 350, 380, 430)
var += 'high', GammaMembership(650, 1000), <step>

```

`<step>` represents the distance between two elements of the domain limited by `var`. Is optional.

> See `membership` submodule for details about membership functions

To create fuzzy systems with rules use:

```python
mamdani = Mamdani()
mamdani += (
    var.Is('normal'),
    target.Is('high')
)
mamdani += (
    var.Is('normal') & second_var.Is('good'),
    target.Is('low')
)
mamdani += (
    var.Is('normal') | second_var.Is('good'),
    target.Is('regular')
)
```

> See `systems` submodule for details about the implemented systens.

To use the system:

```python
result = mamdani.infer( centroid_defuzzification, graph,
            var=var,
            second_var=second_var
        )

print(result)
```

> Set `graph=True` to see graphs of fuzzy sets created

> Also check `defuzzification` submodule for more defuzification functions

### Note

Check `doc/Informe.pdf` to see a full explanation of the ideas used to build the agents and the environment. The document is in Spanish.

## Author ✒️

- **Miguel Tenorio Potrony** -------> [stdevAntiD2ta](https://github.com/stdevAntiD2ta)

## License 📄

This project is under the License (MIT License) - see the file [LICENSE.md](LICENSE.md) for details.
