from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExternallyAccessibleAzureBlobContainerFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	accessibility: Optional[AzureAccessType | str] = Field(alias="accessibility",default=None,)
	encryptionManagedBy: Optional[AzureEncryption | str] = Field(alias="encryptionManagedBy",default=None,)
	storageAccount: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="storageAccount",default=None,)

from .azure_access_type import AzureAccessType
from .azure_encryption import AzureEncryption
from .authorization_system_resource import AuthorizationSystemResource

