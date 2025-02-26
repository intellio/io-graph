from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationLinkedObjects(BaseModel):
	manager: Optional[SynchronizationJobSubject] = Field(default=None,alias="manager",)
	members: list[SynchronizationJobSubject] = Field(alias="members",)
	owners: list[SynchronizationJobSubject] = Field(alias="owners",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject

