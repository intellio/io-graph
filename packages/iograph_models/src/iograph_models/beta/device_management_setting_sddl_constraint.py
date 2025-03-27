from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingSddlConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingSddlConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingSddlConstraint")


