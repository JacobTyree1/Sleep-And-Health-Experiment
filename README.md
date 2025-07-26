# Sleep and Health Data Analysis Project

This project analyzes sleep patterns and their relationship with various health metrics using the Sleep Health and Lifestyle dataset.

## Project Setup with uv

This project uses `uv` for fast Python package management and virtual environment handling.

### Prerequisites

- Python 3.12+
- uv (install with `pip install uv`)

### Getting Started

1. **Clone or navigate to the project directory**
   ```bash
   cd Sleep-And-Health-Experiment
   ```

2. **Activate the virtual environment**
   ```bash
   uv shell
   ```

3. **Install dependencies** (already done during setup)
   ```bash
   uv sync
   ```

4. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

### Project Structure

```
Sleep-And-Health-Experiment/
├── .venv/                    # Virtual environment (created by uv)
├── pyproject.toml           # Project configuration and dependencies
├── uv.lock                  # Locked dependency versions
├── main.py                  # Main entry point
├── DataSciencePractice.ipynb # Jupyter notebook with analysis
├── SleepHealthandLifestyle.csv # Dataset
└── README.md               # This file
```

### Key Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib & seaborn**: Data visualization
- **scikit-learn**: Machine learning
- **jupyter**: Interactive notebooks
- **plotly**: Interactive visualizations

### Dataset

The `SleepHealthandLifestyle.csv` file contains:
- Person demographics (ID, Gender, Age, Occupation)
- Sleep metrics (Duration, Quality, Disorders)
- Health indicators (BMI, Blood Pressure, Heart Rate)
- Lifestyle factors (Physical Activity, Stress Level, Daily Steps)

### Common uv Commands

```bash
# Add a new package
uv add package_name

# Remove a package
uv remove package_name

# Update all packages
uv update

# List installed packages
uv list

# Run a script
uv run python script.py

# Activate virtual environment
uv shell
```

### Analysis Workflow

1. Open `DataSciencePractice.ipynb` in Jupyter
2. Explore the dataset structure
3. Perform exploratory data analysis
4. Create visualizations
5. Build predictive models
6. Document findings

## Contributing

When adding new dependencies, use `uv add package_name` to automatically update `pyproject.toml` and `uv.lock`.