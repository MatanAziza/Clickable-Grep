# Clickable-Grep

This small code allows you to grep easily (on Linux) from your terminal into a folder and display hyperlinks to the found files.

## Installation

You can either git clone this repository using

```bash
git clone <https_key>
```

or by downloading the latest release.

## How to run

To run, you have 2 run options:

- 1

```bash
./find_files.py <args>
```

- 2

```bash
python3 find_files.py <args>
```

As for the arguments to provide:

- 1: Provide only the argument you're looking for, and the grep will search in the current directory and subdirectories:

### Command

```bash
python3 find_files.py arg_1
```

### Result

```terminal
<span style="color: green">File n°1: GardenGuardian/ex4/ft_raise_errors.py</span>
<span style="color: green">File n°2: CodeCultivation/ex4/ft_garden_security.py</span>
<span style="color: green">File n°3: GardenGuardian/ex0/ft_first_exception.py</span>
<span style="color: green">File n°4: CodeCultivation/ex5/ft_plant_types.py</span>
<span style="color: green">File n°5: GardenGuardian/ex2/ft_custom_errors.py</span>
<span style="color: green">File n°6: GardenGuardian/ex3/ft_finally_block.py</span>
<span style="color: green">File n°7: CodeCultivation/ex0/ft_garden_intro.py</span>
<span style="color: green">File n°8: GardenGuardian/ex5/ft_garden_management.py</span>
```

