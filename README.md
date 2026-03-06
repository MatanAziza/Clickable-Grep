# Clickable-Grep

This small python program allows you to grep easily (on Linux) from your terminal into a folder and display hyperlinks to the found files.

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
File n°1: GardenGuardian/ex4/ft_raise_errors.py
File n°2: CodeCultivation/ex4/ft_garden_security.py
File n°3: GardenGuardian/ex0/ft_first_exception.py
File n°4: CodeCultivation/ex5/ft_plant_types.py
File n°5: GardenGuardian/ex2/ft_custom_errors.py
File n°6: GardenGuardian/ex3/ft_finally_block.py
```

- 2: Provide the argument you're looking for, as well as the path you want to look into.

### Command

```bash
python3 find_files.py arg_1 path
```

### Result

```terminal
Same result as 1st option.
```

