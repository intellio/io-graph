from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJobRestartCriteria(BaseModel):
	resetScope: Optional[SynchronizationJobRestartScope] = Field(default=None,alias="resetScope",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_job_restart_scope import SynchronizationJobRestartScope

