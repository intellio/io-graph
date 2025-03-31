from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AzureRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.azureRoleDefinition"] = Field(alias="@odata.type",)
	assignableScopes: Optional[list[str]] = Field(alias="assignableScopes", default=None,)
	azureRoleDefinitionType: Optional[AzureRoleDefinitionType | str] = Field(alias="azureRoleDefinitionType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)

from .azure_role_definition_type import AzureRoleDefinitionType
