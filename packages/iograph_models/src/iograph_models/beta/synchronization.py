from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Synchronization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	secrets: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(alias="secrets", default=None,)
	jobs: Optional[list[SynchronizationJob]] = Field(alias="jobs", default=None,)
	templates: Optional[list[SynchronizationTemplate]] = Field(alias="templates", default=None,)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
from .synchronization_job import SynchronizationJob
from .synchronization_template import SynchronizationTemplate

