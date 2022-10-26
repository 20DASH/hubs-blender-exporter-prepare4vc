from bpy.props import BoolProperty, FloatProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType

class ProxTrigAnim(HubsComponent):
    _definition = {
        'name': 'proxtrig-anim',
        'display_name': 'Proximity Animation Trigger',
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

    minDist: FloatProperty(
        name="Minimum Distance",
        default=0.0,
        min=0.0)

    # shouldReset: BoolProperty(
    #     name="Should File Reset", description="Reset file each time the play distance is entered", default=False)

    shouldLoop: BoolProperty(
        name="Should Anim Loop", description="Loop animation file when enabled", default=False)

    # onClips
    onClips: StringProperty(
        name="On Clips", description="Clip to be played when within play dist", default="")

    # offClips
    offClips: StringProperty(
        name="Off Clips", description="Clip to be played when outside play dist", default="")