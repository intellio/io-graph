from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileEncryptionInfo(BaseModel):
	encryptionKey: Optional[str] = Field(default=None,alias="encryptionKey",)
	fileDigest: Optional[str] = Field(default=None,alias="fileDigest",)
	fileDigestAlgorithm: Optional[str] = Field(default=None,alias="fileDigestAlgorithm",)
	initializationVector: Optional[str] = Field(default=None,alias="initializationVector",)
	mac: Optional[str] = Field(default=None,alias="mac",)
	macKey: Optional[str] = Field(default=None,alias="macKey",)
	profileIdentifier: Optional[str] = Field(default=None,alias="profileIdentifier",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


