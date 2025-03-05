from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeNotificationEncryptedContent(BaseModel):
	data: Optional[str] = Field(alias="data",default=None,)
	dataKey: Optional[str] = Field(alias="dataKey",default=None,)
	dataSignature: Optional[str] = Field(alias="dataSignature",default=None,)
	encryptionCertificateId: Optional[str] = Field(alias="encryptionCertificateId",default=None,)
	encryptionCertificateThumbprint: Optional[str] = Field(alias="encryptionCertificateThumbprint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


