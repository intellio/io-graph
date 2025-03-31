from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityEpicSMSUnlinkRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.epicSMSUnlinkRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.epicSMSUnlinkRecord")

