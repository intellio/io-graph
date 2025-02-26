from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceUserProcessingResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IdentityGovernanceUserProcessingResult] = Field(alias="value",)

from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult

