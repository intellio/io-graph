from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppLogCollectionDownloadDetails(BaseModel):
	appLogDecryptionAlgorithm: Optional[str | AppLogDecryptionAlgorithm] = Field(alias="appLogDecryptionAlgorithm",default=None,)
	decryptionKey: Optional[str] = Field(alias="decryptionKey",default=None,)
	downloadUrl: Optional[str] = Field(alias="downloadUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

