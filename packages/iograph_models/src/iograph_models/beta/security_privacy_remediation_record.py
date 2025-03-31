from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPrivacyRemediationRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyRemediationRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyRemediationRecord")

