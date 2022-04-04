"""This module builds a diagram based on a plotly library, making it
easy to use in a web environment."""

from typing import Union
from validate import *
import plotly.express as px

def make_html_diagram(
    df, x: str, y: list, username: str, title: str = None,
    charts_colors: Union[str, list, tuple] = None, x_label: str = None,
    y_label :str = None, legend_label :str = None, text_color: str = None,
    title_text_color: str = None, legend_text_color: str = None,
    bg_color: str = 'white'
) -> None:

    """Builds a diagram using the parameters given to it to display
both the design and the data. It creates or updates the .html file
with the given username."""

    if (is_string(x, username) and is_list(y) and
        is_string_list_tuple_or_none(charts_colors) and
        is_string_or_none(
            title, x_label, y_label, legend_label, text_color,
            title_text_color, legend_text_color, bg_color
        )
    ):
        fig = px.line(
            data_frame = df,
            x = x,
            y = y,
            title = title,
            color_discrete_sequence = charts_colors
        )

        fig.update_layout(
            xaxis_title = x_label,
            yaxis_title = y_label,
            legend_title = legend_label,
            title = {
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            font_color = text_color,
            title_font_color = title_text_color,
            legend_font_color = legend_text_color,
            paper_bgcolor = bg_color,
            font_size = 13,
            legend_font_size = 14,
            title_font_size = 20
        )

        fig.write_html('{}.html'.format(username), auto_open=True)
    return None
