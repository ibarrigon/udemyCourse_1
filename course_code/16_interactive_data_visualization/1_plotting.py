from bokeh.plotting import figure, show, output_file
from datetime import datetime
import pandas

moving_object_times = pandas.read_csv('./course_code/14_computer_vision/files/movingObjectsValues.csv')

graph = figure(
    x_axis_type = 'datetime', 
    min_height = 100, 
    min_width = 500, 
    title = 'Motion graph', 
    sizing_mode = 'stretch_both'
)

graph.yaxis.minor_tick_line_color = None
graph.ygrid[0].ticker.desired_num_ticks = 1

quad_plot = graph.quad(
    left = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in moving_object_times['Start']], 
    right = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in moving_object_times['End']], 
    bottom = 0, 
    top = 1, 
    color = 'green'
)

output_file('./course_code/14_computer_vision/generated/quadrant_data_graph.html')
show(graph)