![logo](./MppiTorch.png)

A fast and modular MPPI implementation with Halton spline sampling 

## Credits

Much of the backbone of the mppi implementation is based on [pytorch_mppi](https://github.com/UM-ARM-Lab/pytorch_mppi), however it has been modified with addition sampling modes (e.g. Halton spline sampling) and support for ancillary controllers (priors) by [Corrado Pezzato](https://github.com/cpezzato), [Elia Trevisan](https://github.com/eliatrevisan) and [Chadi Salmi](https://github.com/c-salmi).

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

## Cite
This repository was originally developed for our paper [Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations](https://sites.google.com/view/mppi-isaac/). You can find that code [here](https://github.com/tud-airlab/mppi-isaac). If relevant, consider citing:
```bash
@misc{pezzato2023samplingbased,
      title={Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations}, 
      author={Corrado Pezzato and Chadi Salmi and Max Spahn and Elia Trevisan and Javier Alonso-Mora and Carlos Hernandez Corbato},
      year={2023},
      eprint={2307.09105},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```
We also recently added the possibility of biasing the sampling distribution with ancillary controllers (or priors), as in [Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers](https://autonomousrobots.nl/paper_websites/biased-mppi). Examples of how to use prior controllers with this repository can be found [here](https://github.com/eliatrevisan/biased-mppi). If you use this feature, consider citing:
```bash
@ARTICLE{trevisan2024biased,
  author={Trevisan, Elia and Alonso-Mora, Javier},
  journal={IEEE Robotics and Automation Letters}, 
  title={Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers}, 
  year={2024},
  volume={9},
  number={6},
  pages={5871-5878},
  keywords={Costs;Planning;Monte Carlo methods;Mathematical models;Optimal control;Vehicle dynamics;Trajectory;Motion and path planning;optimization and optimal control;collision avoidance;sampling-based MPC;MPPI},
  doi={10.1109/LRA.2024.3397083}}
```

