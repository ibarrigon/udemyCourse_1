[go back](../course_code.md)

# Data Visualization

A library to create plots and data visualization. It's interactive.

[Documentation](https://docs.bokeh.org/en/latest/)

## Libraries

+ pandas
+ bokeh

## Read data

In the course the parsed date its in read_csv, but it doesn't work for this implementation and Docker image. 
The code you can read in the course it's:
`
externalData = pandas.read_csv('./files/adbe.csv', parse_dates = ['Date'], date_format = lambda dt: datetime.datetime.strptime(dt, '%d-%b-%y'))
`

## Styles

This link has related info to styles [Review styles](https://docs.bokeh.org/en/latest/docs/user_guide/styling.html) but
it needs a revision due the deprecated code.

## Dates

To work with dates, we can read [this website](https://www.programiz.com/python-programming/datetime/strptime)

## Graphs

The responsive parameter was removed several years ago. We need to uses sizing_mode with values:
+ "scale_width"
+ "stretch_both"
+ "fixed"
+ "stretch_width"
+ "stretch_both"
