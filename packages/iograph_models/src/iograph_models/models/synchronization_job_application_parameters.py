from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationJobApplicationParameters(BaseModel):
	ruleId: Optional[str] = Field(default=None,alias="ruleId",)
	subjects: list[SynchronizationJobSubject] = Field(alias="subjects",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_job_subject import SynchronizationJobSubject

