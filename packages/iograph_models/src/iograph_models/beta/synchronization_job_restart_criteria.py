from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJobRestartCriteria(BaseModel):
	resetScope: Optional[SynchronizationJobRestartScope | str] = Field(alias="resetScope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_job_restart_scope import SynchronizationJobRestartScope

