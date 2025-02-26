from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesDirectorySynchronization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configuration: Optional[OnPremisesDirectorySynchronizationConfiguration] = Field(default=None,alias="configuration",)
	features: Optional[OnPremisesDirectorySynchronizationFeature] = Field(default=None,alias="features",)

from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

