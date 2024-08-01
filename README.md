# Chaotic Pendulum

## Motivation
This project aims to model and animate a double pendulum using Euler's equations of motion with given initial conditions. The `scipy.integrate` library's ODE integration function is used to solve the pair of coupled 2nd order differential equations of motion. This project was inspired by a course taken on "Nonlinear Dynamics and Chaos", where the concepts learned sparked an interest in visualizing chaotic systems through coding.

## Introduction
A double pendulum is a system of two pendulums connected end to end. This system demonstrates how small variations in initial conditions can lead to large changes in the system's behavior.

![Double pendulum](https://media.licdn.com/dms/image/D5612AQFmaZYmrGOpeQ/article-cover_image-shrink_600_2000/0/1685585399017?e=2147483647&v=beta&t=Z-AzQWWhOOjpEuA1HL3xruBeq6cbs9XLQ-5pCvyupSg)

A complete formulation describing how to write the Lagrange and then the system's equations of motion can be found [here](https://www.physics.umd.edu/hep/drew/pendulum2.html).

## Difference between a Double Pendulum and a Simple Pendulum
A double pendulum differs from a simple pendulum not only because it is a 2-mass system but also due to its sensitivity to initial conditions. While a simple pendulum's motion is predictable using Lagrangian mechanics and Euler's equations of motion, a double pendulum's motion shows non-linear behavior and chaotic unpredictability for large displacements.

## Paradox of Chaos
Even with the equations of motion available, the double pendulum system remains unpredictable due to its sensitivity to initial conditions. Small differences in initial conditions lead to dramatically different trajectories over time. This phenomenon, known as chaos, is prevalent in various scientific and engineering fields.

**Note:** CHAOS ≠ RANDOMNESS. If two double pendulums have the exact same initial conditions, they will trace the same path. However, in practice, it's impossible to set identical initial conditions, making the path unpredictable.

## Files in Repository

- `double_pendulum.py`: Main script to simulate and animate the double pendulum.
- `README.md`: Project overview and instructions.

## Requirements

- Python 3.11.0
- Libraries: numpy, scipy, matplotlib, matplotlib.animation

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/chaotic-pendulum.git
    cd chaotic-pendulum
    ```

2. Install the required libraries:
    ```bash
    pip install numpy scipy matplotlib
    ```

## Running the Project

1. Ensure `double_pendulum.py` is in the root directory.
2. Run the script to simulate and animate the double pendulum.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### References

1. [Formulation of the Double Pendulum Equations of Motion](https://www.physics.umd.edu/hep/drew/pendulum2.html)
2. Image: [Double Pendulum](https://rjallain.medium.com/finding-the-equation-of-motion-for-a-double-pendulum-cff2635f99bd)
