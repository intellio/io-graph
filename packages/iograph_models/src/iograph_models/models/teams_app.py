from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	distributionMethod: Optional[TeamsAppDistributionMethod] = Field(default=None,alias="distributionMethod",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	appDefinitions: Optional[list[TeamsAppDefinition]] = Field(default=None,alias="appDefinitions",)

from .teams_app_distribution_method import TeamsAppDistributionMethod
from .teams_app_definition import TeamsAppDefinition

