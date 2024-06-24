# AUTOGENERATED! DO NOT EDIT! File to edit: ../03d_deashboard2.ipynb.

# %% auto 0
__all__ = ['desc_and_ctrl_box', 'data_box', 'main_widget', 'data_and_plot', 'text_boxes', 'source', 'target', 'link']

# %% ../03d_deashboard2.ipynb 2
import ipywidgets as widgets

from .widgets_autoui import controls
from .widgets_classes import DataAndPlot, TextBoxes

# %% ../03d_deashboard2.ipynb 4
# Create a VBox to hold the description and control widgets
desc_and_ctrl_box = widgets.VBox()

# Add a vertical box holding both table and plot visualizations of selected data
data_box = widgets.VBox()

# The entire widget
main_widget = widgets.HBox(children = (desc_and_ctrl_box, data_box))

# %% ../03d_deashboard2.ipynb 8
data_and_plot = DataAndPlot()
text_boxes = TextBoxes()

desc_and_ctrl_box.children = (text_boxes, controls)
data_box.children = (data_and_plot.data_output, data_and_plot.plot_output)

# %% ../03d_deashboard2.ipynb 10
source = (controls, "_value")
target = (data_and_plot, "smoothing_info")
link = widgets.link(source, target)
