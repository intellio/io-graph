from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFileDetails(BaseModel):
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	filePath: Optional[str] = Field(alias="filePath", default=None,)
	filePublisher: Optional[str] = Field(alias="filePublisher", default=None,)
	fileSize: Optional[int] = Field(alias="fileSize", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	sha1: Optional[str] = Field(alias="sha1", default=None,)
	sha256: Optional[str] = Field(alias="sha256", default=None,)
	signer: Optional[str] = Field(alias="signer", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

