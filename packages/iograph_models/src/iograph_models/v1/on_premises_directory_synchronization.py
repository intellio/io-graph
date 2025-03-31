from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPremisesDirectorySynchronization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onPremisesDirectorySynchronization"] = Field(alias="@odata.type",)
	configuration: Optional[OnPremisesDirectorySynchronizationConfiguration] = Field(alias="configuration", default=None,)
	features: Optional[OnPremisesDirectorySynchronizationFeature] = Field(alias="features", default=None,)

from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature
