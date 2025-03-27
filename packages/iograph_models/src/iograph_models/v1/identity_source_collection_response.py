from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IdentitySourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AzureActiveDirectoryTenant, CrossCloudAzureActiveDirectoryTenant, DomainIdentitySource, ExternalDomainFederation, SocialIdentitySource],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .azure_active_directory_tenant import AzureActiveDirectoryTenant
from .cross_cloud_azure_active_directory_tenant import CrossCloudAzureActiveDirectoryTenant
from .domain_identity_source import DomainIdentitySource
from .external_domain_federation import ExternalDomainFederation
from .social_identity_source import SocialIdentitySource

