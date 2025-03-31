from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintDocumentUploadProperties(BaseModel):
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	documentName: Optional[str] = Field(alias="documentName", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

