from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTaskReportCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IdentityGovernanceTaskReport] = Field(alias="value",)

from .identity_governance_task_report import IdentityGovernanceTaskReport

