from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPrivacyDataMinimizationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyDataMinimizationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyDataMinimizationRecord")


