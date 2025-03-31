from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPrivacyDigestEmailRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyDigestEmailRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyDigestEmailRecord")

