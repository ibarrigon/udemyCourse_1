from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from datetime import datetime
import pandas

moving_object_times = pandas.read_csv('./course_code/14_computer_vision/files/movingObjectsValues.csv')

moving_object_times['Start'] = moving_object_times['Start'].apply(lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f'))
moving_object_times['End'] = moving_object_times['End'].apply(lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f'))
moving_object_times['Start_string'] = moving_object_times['Start'].apply(lambda date: datetime.strftime(date, '%Y-%m-%d %H:%M:%S'))
moving_object_times['End_string'] = moving_object_times['End'].apply(lambda date: datetime.strftime(date, '%Y-%m-%d %H:%M:%S'))

graph = figure(
    x_axis_type = 'datetime', 
    height = 100, 
    min_width = 500, 
    title = 'Motion graph', 
    sizing_mode = 'stretch_both'
)

graph.yaxis.minor_tick_line_color = None
graph.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips = [('Start', '@Start_string'), ('End', '@End_string')])
graph.add_tools(hover)

quad_plot = graph.quad(left = 'Start', right = 'End', bottom = 0, top = 1, color = 'green')

output_file('./course_code/14_computer_vision/generated/quadrant_with_models.html')
show(graph)