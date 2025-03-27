from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	configuration: Optional[OnPremisesDirectorySynchronizationConfiguration] = Field(alias="configuration", default=None,)
	features: Optional[OnPremisesDirectorySynchronizationFeature] = Field(alias="features", default=None,)

from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

