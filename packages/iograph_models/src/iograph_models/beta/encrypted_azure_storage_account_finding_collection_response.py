from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EncryptedAzureStorageAccountFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EncryptedAzureStorageAccountFinding]] = Field(alias="value", default=None,)

from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding

