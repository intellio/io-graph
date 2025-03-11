from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTaskReportSummary(BaseModel):
	failedTasks: Optional[int] = Field(alias="failedTasks",default=None,)
	successfulTasks: Optional[int] = Field(alias="successfulTasks",default=None,)
	totalTasks: Optional[int] = Field(alias="totalTasks",default=None,)
	unprocessedTasks: Optional[int] = Field(alias="unprocessedTasks",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


