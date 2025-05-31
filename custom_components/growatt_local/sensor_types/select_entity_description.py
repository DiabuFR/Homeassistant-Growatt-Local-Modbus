from dataclasses import dataclass

from homeassistant.components.select import SelectEntityDescription


@dataclass
class GrowattSelectRequiredKeysMixin:
    """Mixin for required keys."""
    key: str
    options_values: dict[str,int]

@dataclass
class GrowattSelectEntityDescription(SelectEntityDescription, GrowattSelectRequiredKeysMixin):
    """Describes Growatt sensor entity."""

