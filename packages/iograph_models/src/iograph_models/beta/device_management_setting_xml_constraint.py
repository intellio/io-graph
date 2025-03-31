from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementSettingXmlConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingXmlConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingXmlConstraint")

