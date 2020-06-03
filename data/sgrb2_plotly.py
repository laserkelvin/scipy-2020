
import pandas as pd
from plotly import graph_objs as go

data = pd.read_csv("sgrb2_data.tsv", delim_whitespace=True, comment="#")
data.columns = ["Frequency", "Temperature"]
data.sort_values("Frequency", inplace=True)
# data["Frequency"] *= 1e3

fig = go.Figure(
    data=go.Scatter(
        x=data["Frequency"],
        y=data["Temperature"],
        line={"color": "#f03b20"}
    ),
    layout=go.Layout(
        # title="Sgr B2(N) — Belloche+2013",
        xaxis_title="Frequency (GHz)",
        yaxis_title="Temperature (K)",
        font={"family": "Roboto", "size": 24},
        height=600,
        width=800,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        # updatemenus=[dict(
        #     type="buttons",
        #     buttons=[
        #         {
        #         "args": [None, {"frame": {"duration": 10000, "redraw": True},
        #                         "fromcurrent": True, "transition": {"duration": 5000,
        #                                                             "easing": "quadratic-in-out"}}],
        #         "label": "Zoom",
        #         "method": "animate"
        #     },
        #         ])],
        xaxis={"range": (90, 94)},
        yaxis={"range": (-1, 4), "autorange": False}
    ),
    # frames=[
    #     go.Frame(
    #         data=[go.Scatter(x=data["Frequency"], y=data["Temperature"])],
    #         layout=go.Layout(xaxis={"range": (90, 98)}, yaxis={"range": (-1, 4)})
    #     ),
    #     go.Frame(
    #         data=[go.Scatter(x=data["Frequency"], y=data["Temperature"])],
    #         layout=go.Layout(xaxis={"autorange": True, "range": (80, 117)}, yaxis={"autorange": True})
    #     ),
    # ]
)

# fig.update_xaxes(range=[90, 98])
# fig.update_yaxes(range=[-1, 4])

with open("sgrb2.html", "w+") as write_file:
    write_file.write(fig.to_html(include_plotlyjs="cdn"))
