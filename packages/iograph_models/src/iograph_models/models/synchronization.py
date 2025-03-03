from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Synchronization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	secrets: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(default=None,alias="secrets",)
	jobs: Optional[list[SynchronizationJob]] = Field(default=None,alias="jobs",)
	templates: Optional[list[SynchronizationTemplate]] = Field(default=None,alias="templates",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
from .synchronization_job import SynchronizationJob
from .synchronization_template import SynchronizationTemplate

