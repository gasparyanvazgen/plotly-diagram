## Plotly diagram using python programming language

> [Click here](https://vazgen-gasparyan.github.io/plotly-diagram/vazgen-gasparyan) to see what result you will get using this module.

<hr/>

If you do not know how to do this, follow these steps.

1. Download requirements for this module via pip։ `pip install -r requirements.txt`.
2. Create a new file with .py extension: *filename.py*.
3. Import the module in the file to use the diagram making function։ `import diagram` or `from diagram import make_html_diagram`.
4. If you used this one `import diagram`, call the function this way `diagram.make_html_diagram()`, otherwise this way `make_html_diagram()`.
5. Since the function requires a **data frame**, we can use the **pandas** library. You can download it with `pip install pandas`.
6. If you use a file with .csv extension to store your data, you can easily get a diagram that matches that data. Just import the **pandas** library to create a data frame from a .csv file: `import pandas as pd` and `df = pd.read_csv("filename.csv")`. If you do not have a .csv file, do not worry, you can get the data frame in another way, so [click here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).
7. If you have everything, it is your turn to make a diagram.

```python
    make_html_diagram(
        df = df, x = "local_date_time",
        y = ["air_humidity", "humidity", "temperature"],
        username = "vazgen-gasparyan", title = "Plotly diagram",
        charts_colors = ["#52A8DE", "#60E450", "#E03737"],
        x_label = "Date and time", y_label = "Data sizes",
        legend_label = "Chart lines", text_color = "#6805AA",
        title_text_color = "#7AC812", legend_text_color = "#1D5570"
    )
```
