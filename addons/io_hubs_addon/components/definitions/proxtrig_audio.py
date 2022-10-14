from bpy.props import BoolProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType


class Billboard(HubsComponent):
    _definition = {
        'name': 'proxtrig-audio',
        'display_name': 'Proximity Audio Trigger',
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'OUTLINER_OB_SPEAKER'
    }

    playDist: FloatProperty(
        name="Play Distance",
        default=3.0,
        min=0.0)

    pauseDist: FloatProperty(
        name="Pause Distance",
        default=4.0,
        min=0.0)

    shouldReset: BoolProperty(
        name="Should File Reset", description="Reset file each time the play distance is entered", default=False)
