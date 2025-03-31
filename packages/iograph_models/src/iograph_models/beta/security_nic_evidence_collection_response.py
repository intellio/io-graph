from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityNicEvidenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityNicEvidence]] = Field(alias="value", default=None,)

from .security_nic_evidence import SecurityNicEvidence
