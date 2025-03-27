from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDisplayConfiguration(BaseModel):
	configuredDisplays: Optional[list[TeamworkConfiguredPeripheral]] = Field(alias="configuredDisplays", default=None,)
	displayCount: Optional[int] = Field(alias="displayCount", default=None,)
	inBuiltDisplayScreenConfiguration: Optional[TeamworkDisplayScreenConfiguration] = Field(alias="inBuiltDisplayScreenConfiguration", default=None,)
	isContentDuplicationAllowed: Optional[bool] = Field(alias="isContentDuplicationAllowed", default=None,)
	isDualDisplayModeEnabled: Optional[bool] = Field(alias="isDualDisplayModeEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_configured_peripheral import TeamworkConfiguredPeripheral
from .teamwork_display_screen_configuration import TeamworkDisplayScreenConfiguration

