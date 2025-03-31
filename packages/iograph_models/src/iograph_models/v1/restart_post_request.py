from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestartPostRequest(BaseModel):
	criteria: Optional[SynchronizationJobRestartCriteria] = Field(alias="criteria", default=None,)

from .synchronization_job_restart_criteria import SynchronizationJobRestartCriteria
