from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestartPostRequest(BaseModel):
	criteria: Optional[SynchronizationJobRestartCriteria] = Field(default=None,alias="criteria",)

from .synchronization_job_restart_criteria import SynchronizationJobRestartCriteria

