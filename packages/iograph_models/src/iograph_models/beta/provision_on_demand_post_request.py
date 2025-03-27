from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Provision_on_demandPostRequest(BaseModel):
	parameters: Optional[list[SynchronizationJobApplicationParameters]] = Field(alias="parameters", default=None,)

from .synchronization_job_application_parameters import SynchronizationJobApplicationParameters

