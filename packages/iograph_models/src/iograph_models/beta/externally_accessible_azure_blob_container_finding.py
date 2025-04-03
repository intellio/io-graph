from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExternallyAccessibleAzureBlobContainerFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externallyAccessibleAzureBlobContainerFinding"] = Field(alias="@odata.type", default="#microsoft.graph.externallyAccessibleAzureBlobContainerFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibility: Optional[AzureAccessType | str] = Field(alias="accessibility", default=None,)
	encryptionManagedBy: Optional[AzureEncryption | str] = Field(alias="encryptionManagedBy", default=None,)
	storageAccount: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="storageAccount", default=None,discriminator="odata_type", )

from .azure_access_type import AzureAccessType
from .azure_encryption import AzureEncryption
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
