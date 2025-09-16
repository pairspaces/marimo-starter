import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import httpx
    import json
    import altair as alt
    return alt, httpx, json, pd


@app.cell
def _(alt, httpx, json, mo, pd):
    cars = pd.DataFrame(json.loads(
      httpx.get('https://vega.github.io/vega-datasets/data/cars.json').read()
    ))

    chart = mo.ui.altair_chart(alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin'
    ))
    return (chart,)


@app.cell
def _(chart, mo):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
