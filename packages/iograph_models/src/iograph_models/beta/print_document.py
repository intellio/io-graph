from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrintDocument(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	configuration: Optional[PrinterDocumentConfiguration] = Field(alias="configuration", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	downloadedDateTime: Optional[datetime] = Field(alias="downloadedDateTime", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	uploadedDateTime: Optional[datetime] = Field(alias="uploadedDateTime", default=None,)

from .printer_document_configuration import PrinterDocumentConfiguration

