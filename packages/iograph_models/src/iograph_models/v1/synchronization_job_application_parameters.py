from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJobApplicationParameters(BaseModel):
	ruleId: Optional[str] = Field(alias="ruleId", default=None,)
	subjects: Optional[list[SynchronizationJobSubject]] = Field(alias="subjects", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .synchronization_job_subject import SynchronizationJobSubject

