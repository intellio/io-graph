from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ElevationRequestApplicationDetail(BaseModel):
	fileDescription: Optional[str] = Field(alias="fileDescription", default=None,)
	fileHash: Optional[str] = Field(alias="fileHash", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	filePath: Optional[str] = Field(alias="filePath", default=None,)
	productInternalName: Optional[str] = Field(alias="productInternalName", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	productVersion: Optional[str] = Field(alias="productVersion", default=None,)
	publisherCert: Optional[str] = Field(alias="publisherCert", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

