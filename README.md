![logo](./MppiTorch.png)

A fast and modular MPPI implementation with Halton spline sampling 

## Credits

Much of the backbone of the mppi implementation is based on [pytorch_mppi](https://github.com/UM-ARM-Lab/pytorch_mppi), however it has been modified with addition sampling modes (e.g. Halton spline sampling) by [Corrado Pezzato](https://github.com/cpezzato), [Elia Trevisan](https://github.com/eliatrevisan) and [Chadi Salmi](https://github.com/c-salmi).

## Structure

The project is structured as follows:

- `examples/`: Contains the point robot example.
- `mppi_torch/`: Contains the implementation of the MPPI algorithm and its utilities.
- `pyproject.toml` and `poetry.lock`: Configuration files for project dependencies.

## Installation

To install the project, follow these steps:

```sh
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd <project-directory>

# Install dependencies
poetry install
```

## Usage

To run the point robot example:

```
cd examples/point_robot
python run.py
```

## Contributing

Contributions are welcome. Please submit a pull request.