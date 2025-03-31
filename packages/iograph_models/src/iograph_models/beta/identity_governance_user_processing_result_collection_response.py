from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceUserProcessingResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityGovernanceUserProcessingResult]] = Field(alias="value", default=None,)

from .identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
