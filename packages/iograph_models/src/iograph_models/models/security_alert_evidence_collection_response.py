from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAlertEvidenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityAlertEvidence] = Field(alias="value",)

from .security_alert_evidence import SecurityAlertEvidence

