from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMsticNationStateNotificationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.msticNationStateNotificationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.msticNationStateNotificationRecord")

