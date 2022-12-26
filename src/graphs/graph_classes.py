import plotly.express as px


class Graphs:
    def windrose(self, slider_number):
        df = px.data.wind()
        df["frequency"] = df["frequency"] * slider_number

        fig = px.bar_polar(
            df,
            r="frequency",
            theta="direction",
            color="strength",
            template="plotly_dark",
            color_discrete_sequence=px.colors.sequential.Plasma_r,
        )
        return fig

    def iris(self, slider_number):
        df = px.data.iris()
        fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
        return fig
