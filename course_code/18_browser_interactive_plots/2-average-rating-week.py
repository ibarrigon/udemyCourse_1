import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

def get_data():
    data = pandas.read_csv('./course_code/18_browser_interactive_plotsfiles/reviews.csv', parse_dates = ['Timestamp'])
    data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
    
    return data.groupby(['Week']).mean('Rating')

chart_definition = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Day Ratings Mean'
    },
    subtitle: {
        text: 'Courses ratings'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Dates'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average rating'
        },
        labels: {
            format: '{value}'
        },
        accesibility: {
            rangeDescription: 'Average'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {}
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
"""

def app():
    webPage = jp.QuasarPage()
    head1 = jp.QDiv(a = webPage, text = 'Analysis of Course Reviews', classes = 'text-h3 text-center q-pa-md')
    paragraph1 = jp.QDiv(a = webPage, text = 'These graphs represent course review analysis')
    chart = jp.HighCharts(a = webPage, options = chart_definition)
    
    data = get_data()    
    
    chart.options.xAxis.categories = list(data.index)
    chart.options.series[0].data = list(data['Rating'])
    
    return webPage

# Just add de fuction's name and juspy make the call.
jp.justpy(app)