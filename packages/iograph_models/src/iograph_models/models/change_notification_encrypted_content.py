from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChangeNotificationEncryptedContent(BaseModel):
	data: Optional[str] = Field(default=None,alias="data",)
	dataKey: Optional[str] = Field(default=None,alias="dataKey",)
	dataSignature: Optional[str] = Field(default=None,alias="dataSignature",)
	encryptionCertificateId: Optional[str] = Field(default=None,alias="encryptionCertificateId",)
	encryptionCertificateThumbprint: Optional[str] = Field(default=None,alias="encryptionCertificateThumbprint",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


