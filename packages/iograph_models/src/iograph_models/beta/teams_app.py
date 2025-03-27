from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	distributionMethod: Optional[TeamsAppDistributionMethod | str] = Field(alias="distributionMethod", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	appDefinitions: Optional[list[TeamsAppDefinition]] = Field(alias="appDefinitions", default=None,)

from .teams_app_distribution_method import TeamsAppDistributionMethod
from .teams_app_definition import TeamsAppDefinition

