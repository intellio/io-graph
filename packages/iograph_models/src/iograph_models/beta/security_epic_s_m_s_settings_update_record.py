from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEpicSMSSettingsUpdateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.epicSMSSettingsUpdateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.epicSMSSettingsUpdateRecord")


