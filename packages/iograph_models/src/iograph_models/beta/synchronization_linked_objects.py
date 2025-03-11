from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationLinkedObjects(BaseModel):
	manager: Optional[SynchronizationJobSubject] = Field(alias="manager",default=None,)
	members: Optional[list[SynchronizationJobSubject]] = Field(alias="members",default=None,)
	owners: Optional[list[SynchronizationJobSubject]] = Field(alias="owners",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject
from .synchronization_job_subject import SynchronizationJobSubject

