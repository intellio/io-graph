from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationLinkedObjects(BaseModel):
	manager: Optional[SynchronizationJobSubject] = Field(default=None,alias="manager",)
	members: Optional[list[SynchronizationJobSubject]] = Field(default=None,alias="members",)
	owners: Optional[list[SynchronizationJobSubject]] = Field(default=None,alias="owners",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject

