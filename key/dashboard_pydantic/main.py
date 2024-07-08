# AUTOGENERATED! DO NOT EDIT! File to edit: ../03d_dashboard2.ipynb.

# %% auto 0
__all__ = ['desc_and_ctrl_box', 'data_box', 'main_widget', 'data_and_plot', 'text_boxes', 'data_accordion', 'source', 'target',
           'link']

# %% ../03d_dashboard2.ipynb 5
import ipywidgets as widgets

from .widgets_autoui import controls
from .widgets_classes import DataAndPlot, TextBoxes

# %% ../03d_dashboard2.ipynb 7
# Create a VBox to hold the description and control widgets
desc_and_ctrl_box = widgets.VBox()

# Add a vertical box holding both table and plot visualizations of selected data
data_box = widgets.VBox()

# The entire widget
main_widget = widgets.HBox(children = (desc_and_ctrl_box, data_box))

# %% ../03d_dashboard2.ipynb 11
data_and_plot = DataAndPlot()
text_boxes = TextBoxes()

data_accordion = widgets.Accordion(children=(data_and_plot.data_output,), titles=("Selected Data",))
desc_and_ctrl_box.children = (text_boxes, controls)
data_box.children = (data_accordion, data_and_plot.plot_output)

# %% ../03d_dashboard2.ipynb 13
source = (controls, "_value")
target = (data_and_plot, "smoothing_info")
link = widgets.link(source, target)

# %% ../03d_dashboard2.ipynb 17
# %answer key/3d/01.py

for widget in controls.di_widgets.values():
    widget.layout.max_width = "250px"