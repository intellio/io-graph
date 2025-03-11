from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EncryptedGcpStorageBucketFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	accessibility: Optional[GcpAccessType | str] = Field(alias="accessibility",default=None,)
	encryptionManagedBy: Optional[GcpEncryption | str] = Field(alias="encryptionManagedBy",default=None,)
	storageBucket: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="storageBucket",default=None,)

from .gcp_access_type import GcpAccessType
from .gcp_encryption import GcpEncryption
from .authorization_system_resource import AuthorizationSystemResource

