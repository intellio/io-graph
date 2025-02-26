from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkforceIntegrationEncryption(BaseModel):
	protocol: Optional[WorkforceIntegrationEncryptionProtocol] = Field(default=None,alias="protocol",)
	secret: Optional[str] = Field(default=None,alias="secret",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .workforce_integration_encryption_protocol import WorkforceIntegrationEncryptionProtocol

