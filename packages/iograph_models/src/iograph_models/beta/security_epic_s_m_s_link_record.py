from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityEpicSMSLinkRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.epicSMSLinkRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.epicSMSLinkRecord")

