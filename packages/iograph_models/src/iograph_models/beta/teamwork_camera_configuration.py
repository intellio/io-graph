from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkCameraConfiguration(BaseModel):
	contentCameraConfiguration: Optional[TeamworkContentCameraConfiguration] = Field(alias="contentCameraConfiguration", default=None,)
	cameras: Optional[list[TeamworkPeripheral]] = Field(alias="cameras", default=None,)
	defaultContentCamera: Optional[TeamworkPeripheral] = Field(alias="defaultContentCamera", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_content_camera_configuration import TeamworkContentCameraConfiguration
from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral

