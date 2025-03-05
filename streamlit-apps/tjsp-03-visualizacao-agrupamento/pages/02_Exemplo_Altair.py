
import streamlit as st

import altair as alt
from vega_datasets import data


def main():
    st.title("Exemplo Altair")
    
    df = data.seattle_weather()

    st.dataframe(df)

    st.header("Preciptation")

    chart = alt.Chart(df).mark_tick().encode(
        x="precipitation"
    )

    # st.altair_chart(chart, theme=None, use_container_width=True)
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    st.header("Histogram")

    chart = alt.Chart(df).mark_bar().encode(
        alt.X('precipitation').bin(),
        y='count()'
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    st.header("Temporal encoding")

    chart = alt.Chart(df).mark_line().encode(
        x='month(date):T',
        y='average(precipitation)'
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
    

    st.header("Temporal encoding: year month")

    chart = alt.Chart(df).mark_line().encode(
        x='yearmonth(date):T',
        y='max(temp_max)',
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    chart = alt.Chart(df).mark_line().encode(
        x='year(date):T',
        y='mean(temp_max)',
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    chart = alt.Chart(df).mark_bar().encode(
        x='mean(temp_max)',
        y='year(date):O',
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    st.header("Transform calculation")
    chart = alt.Chart(df).mark_bar().encode(
        x='mean(temp_range):Q',
        y='year(date):O',
    ).transform_calculate(
        temp_range="datum.temp_max - datum.temp_min"
    )
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

    st.header("Interactive grouped charts")

    scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                  range=['#e7ba52', '#c7c7c7', '#aec7e8', '#1f77b4', '#9467bd'])

    brush = alt.selection_interval()

    points = alt.Chart().mark_point().encode(
        alt.X('temp_max:Q').title('Maximum Daily Temperature (C)'),
        alt.Y('temp_range:Q').title('Daily Temperature Range (C)'),
        color=alt.condition(brush, 'weather:N', alt.value('lightgray'), scale=scale),
        size=alt.Size('precipitation:Q').scale(range=[1, 200])
    ).transform_calculate(
        "temp_range", "datum.temp_max - datum.temp_min"
    ).properties(
        width=600,
        height=400
    ).add_params(
        brush
    )

    bars = alt.Chart().mark_bar().encode(
        x='count()',
        y='weather:N',
        color=alt.Color('weather:N').scale(scale),
    ).transform_calculate(
        "temp_range", "datum.temp_max - datum.temp_min"
    ).transform_filter(
        brush
    ).properties(
        width=600
    )

    chart_concat = alt.vconcat(points, bars, data=df)

    st.altair_chart(chart_concat, theme="streamlit", use_container_width=True)


if __name__ == "__main__" :
    main()