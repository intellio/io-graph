from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppLogCollectionDownloadDetails(BaseModel):
	appLogDecryptionAlgorithm: Optional[AppLogDecryptionAlgorithm] = Field(default=None,alias="appLogDecryptionAlgorithm",)
	decryptionKey: Optional[str] = Field(default=None,alias="decryptionKey",)
	downloadUrl: Optional[str] = Field(default=None,alias="downloadUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

