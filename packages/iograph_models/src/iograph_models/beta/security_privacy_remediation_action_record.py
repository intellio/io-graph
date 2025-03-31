from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPrivacyRemediationActionRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyRemediationActionRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyRemediationActionRecord")

