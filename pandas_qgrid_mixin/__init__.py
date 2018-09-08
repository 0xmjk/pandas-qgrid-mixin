from IPython.display import display, HTML
import qgrid
import pandas as pd

def DataFrame_ipython_display_(self):
    use_qgrid = False
    show_qgrid_options = {}
    try:
        use_qgrid = pd.options.display.use_qgrid
        show_qgrid_options = pd.options.display.show_qgrid_options.d
    except Exception:
        pass

    if use_qgrid:
        widget = qgrid.show_grid(self, **show_qgrid_options)
        return widget._ipython_display_()
    else:
        return display(HTML(self._repr_html_()))

pd.DataFrame._ipython_display_ = DataFrame_ipython_display_
use_qgrid_doc = """
: bool
    Display DataFrames using QgridWidget instead of default HTML.
"""
show_qgrid_options_doc = """
: dict
    Kwargs for qgrid.show_grid()
"""
pd.core.config.register_option("display.use_qgrid", True, doc=use_qgrid_doc)
pd.core.config.register_option("display.show_qgrid_options", {}, doc=show_qgrid_options_doc)
