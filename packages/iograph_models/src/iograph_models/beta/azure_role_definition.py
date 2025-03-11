from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureRoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignableScopes: Optional[list[str]] = Field(alias="assignableScopes",default=None,)
	azureRoleDefinitionType: Optional[AzureRoleDefinitionType | str] = Field(alias="azureRoleDefinitionType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)

from .azure_role_definition_type import AzureRoleDefinitionType

