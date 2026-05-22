# ReFly

ReFly is an early-stage reinforcement learning project for UAV autonomy.
The goal is to build a clean, testable codebase for training and evaluating
flight agents in simulation before moving toward real-world deployment.

## What this repository will contain

- **Agents** for training, inference, and evaluation
- **Environments** for simulation-facing flight logic
- **Experiments** for repeatable training runs
- **Tests** for import and behavior coverage as the project grows

## Project structure

```text
refly/
  __init__.py
  agents/
    __init__.py
    base.py
  envs/
    __init__.py
    base.py
experiments/
tests/
```

## Development goals

1. Establish a stable package layout.
2. Define agent and environment interfaces.
3. Add small, focused experiments.
4. Grow test coverage alongside features.

## Getting started

This project is currently a scaffold. When implementation lands, the typical
workflow will be:

1. Create a virtual environment.
2. Install the required dependencies.
3. Run the test suite.
4. Iterate on agents and environments.

## Status

The repository now has a clearer structure and a starting point for continued
development.
