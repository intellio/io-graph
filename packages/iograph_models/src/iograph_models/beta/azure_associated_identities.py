from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AzureAssociatedIdentities(BaseModel):
	all: Optional[list[Annotated[Union[AzureGroup, AzureManagedIdentity, AzureServerlessFunction, AzureServicePrincipal, AzureUser],Field(discriminator="odata_type")]]] = Field(alias="all", default=None,)
	managedIdentities: Optional[list[AzureManagedIdentity]] = Field(alias="managedIdentities", default=None,)
	servicePrincipals: Optional[list[AzureServicePrincipal]] = Field(alias="servicePrincipals", default=None,)
	users: Optional[list[AzureUser]] = Field(alias="users", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .azure_group import AzureGroup
from .azure_managed_identity import AzureManagedIdentity
from .azure_serverless_function import AzureServerlessFunction
from .azure_service_principal import AzureServicePrincipal
from .azure_user import AzureUser
from .azure_managed_identity import AzureManagedIdentity
from .azure_service_principal import AzureServicePrincipal
from .azure_user import AzureUser

