from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationJobSubjectCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SynchronizationJobSubject] = Field(alias="value",)

from .synchronization_job_subject import SynchronizationJobSubject

