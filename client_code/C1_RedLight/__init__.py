from ._anvil_designer import C1_RedLightTemplate
from anvil import *
import anvil.server


class C1_RedLight(C1_RedLightTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
