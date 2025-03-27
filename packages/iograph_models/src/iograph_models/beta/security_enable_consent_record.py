from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEnableConsentRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.enableConsentRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.enableConsentRecord")


