from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentSettingSecretConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementIntentSettingSecretConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementIntentSettingSecretConstraint")


