from data_reader import Measurements, MeasurementsType
import plotly.graph_objects as go


class DataVisualiser:
    def __init__(self):
        self.fig = go.Figure()

    def build_graph(self, measurements: [Measurements]):
        time = list(filter(lambda m: m.measurements_type == MeasurementsType.TIME, measurements))
        y_measurements = list(filter(lambda m: m.measurements_type != MeasurementsType.TIME, measurements))

        for measurement in y_measurements:
            self.fig.add_trace(
                go.Scatter(
                    x=time[0].values,
                    y=measurement.values,
                    name=measurement.name + f' ({measurement.measurements_type.name})',
                    mode='lines+markers',
                    yaxis='y' + str(int(measurement.measurements_type))
                ))

        self.fig.update_layout(
            xaxis=dict(
                domain=[0.2, 0.8]
            ),
            yaxis=dict(
                title=f"{MeasurementsType(1).name}",
                titlefont=dict(color="#1f77b4"),
                tickfont=dict(color="#1f77b4")),

            yaxis2=dict(
                title=f"{MeasurementsType(2).name}",
                titlefont=dict(color="#ff7f0e"),
                tickfont=dict(color="#ff7f0e"),
                anchor="free", overlaying="y",
                side="left", position=0.15),

            yaxis3=dict(
                title=f"{MeasurementsType(3).name}",
                titlefont=dict(color="#d62728"),
                tickfont=dict(color="#d62728"),
                anchor="x", overlaying="y", side="right"),

            yaxis4=dict(
                title=f"{MeasurementsType(4).name}",
                titlefont=dict(color="#9467bd"),
                tickfont=dict(color="#9467bd"),
                anchor="free", overlaying="y",
                side="right", position=0.85)
        )

        # Update layout properties
        self.fig.update_layout(
            title_text="multiple y-axes example"
        )

    def show(self):
        self.fig.show()
