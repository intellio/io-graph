from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalCreationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.servicePrincipalCreationPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.servicePrincipalCreationPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	excludes: Optional[list[ServicePrincipalCreationConditionSet]] = Field(alias="excludes", default=None,)
	includes: Optional[list[ServicePrincipalCreationConditionSet]] = Field(alias="includes", default=None,)

from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet
from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

