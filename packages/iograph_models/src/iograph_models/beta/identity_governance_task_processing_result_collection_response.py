from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTaskProcessingResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityGovernanceTaskProcessingResult]] = Field(alias="value", default=None,)

from .identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult
