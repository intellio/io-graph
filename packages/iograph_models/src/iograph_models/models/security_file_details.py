from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFileDetails(BaseModel):
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	filePath: Optional[str] = Field(default=None,alias="filePath",)
	filePublisher: Optional[str] = Field(default=None,alias="filePublisher",)
	fileSize: Optional[int] = Field(default=None,alias="fileSize",)
	issuer: Optional[str] = Field(default=None,alias="issuer",)
	sha1: Optional[str] = Field(default=None,alias="sha1",)
	sha256: Optional[str] = Field(default=None,alias="sha256",)
	signer: Optional[str] = Field(default=None,alias="signer",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


