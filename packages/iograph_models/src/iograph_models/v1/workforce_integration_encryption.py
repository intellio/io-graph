from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkforceIntegrationEncryption(BaseModel):
	protocol: Optional[WorkforceIntegrationEncryptionProtocol | str] = Field(alias="protocol", default=None,)
	secret: Optional[str] = Field(alias="secret", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .workforce_integration_encryption_protocol import WorkforceIntegrationEncryptionProtocol
