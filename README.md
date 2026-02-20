# Data Science Projects

## Gapminder Clone

### Introduction

This project, **"200 Countries, 200 Years, 4 Minutes,"** recreates the well-known data visualization *Hans Rosling's 200 Countries, 200 Years, 4 Minutes*. We used **pandas** and **sqlite3** to build the database, conducted exploratory validation with **matplotlib**, and finalized the product using **plotly.express**.


### How to Reproduce

- **Install [Miniconda](https://www.anaconda.com/download)** 
- **Create environment from `environment.yml`:**

    ```bash
    conda env create -f environment.yml
    ```

- **Place the four CSV files from the `data/` folder into the `data/` folder in your working directory.**
- **Activate the environment and run `python create_gapminder_db.py`** to create `gapminder.db` in the `data/` folder.
- **Activate the environment and run `python plot_with_px.py`** to generate `gapminder_clone.html`.
