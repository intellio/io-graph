from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityContainerEvidenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityContainerEvidence] = Field(alias="value",)

from .security_container_evidence import SecurityContainerEvidence

