from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EncryptedAzureStorageAccountFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.encryptedAzureStorageAccountFinding"] = Field(alias="@odata.type", default="#microsoft.graph.encryptedAzureStorageAccountFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	encryptionManagedBy: Optional[AzureEncryption | str] = Field(alias="encryptionManagedBy", default=None,)
	storageAccount: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="storageAccount", default=None,discriminator="odata_type", )

from .azure_encryption import AzureEncryption
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
