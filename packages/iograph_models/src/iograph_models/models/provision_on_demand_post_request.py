from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Provision_on_demandPostRequest(BaseModel):
	parameters: Optional[list[SynchronizationJobApplicationParameters]] = Field(default=None,alias="parameters",)

from .synchronization_job_application_parameters import SynchronizationJobApplicationParameters

