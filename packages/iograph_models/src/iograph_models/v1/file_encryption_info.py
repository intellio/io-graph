from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileEncryptionInfo(BaseModel):
	encryptionKey: Optional[str] = Field(alias="encryptionKey", default=None,)
	fileDigest: Optional[str] = Field(alias="fileDigest", default=None,)
	fileDigestAlgorithm: Optional[str] = Field(alias="fileDigestAlgorithm", default=None,)
	initializationVector: Optional[str] = Field(alias="initializationVector", default=None,)
	mac: Optional[str] = Field(alias="mac", default=None,)
	macKey: Optional[str] = Field(alias="macKey", default=None,)
	profileIdentifier: Optional[str] = Field(alias="profileIdentifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

