from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureAssociatedIdentities(BaseModel):
	all: SerializeAsAny[Optional[list[AzureIdentity]]] = Field(alias="all",default=None,)
	managedIdentities: Optional[list[AzureManagedIdentity]] = Field(alias="managedIdentities",default=None,)
	servicePrincipals: Optional[list[AzureServicePrincipal]] = Field(alias="servicePrincipals",default=None,)
	users: Optional[list[AzureUser]] = Field(alias="users",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .azure_identity import AzureIdentity
from .azure_managed_identity import AzureManagedIdentity
from .azure_service_principal import AzureServicePrincipal
from .azure_user import AzureUser

