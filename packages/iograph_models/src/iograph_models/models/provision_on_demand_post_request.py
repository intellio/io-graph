from __future__ import annotations
from pydantic import BaseModel, Field


class Provision_on_demandPostRequest(BaseModel):
	parameters: list[SynchronizationJobApplicationParameters] = Field(alias="parameters",)

from .synchronization_job_application_parameters import SynchronizationJobApplicationParameters

