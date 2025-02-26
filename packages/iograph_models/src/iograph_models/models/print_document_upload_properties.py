from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintDocumentUploadProperties(BaseModel):
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	documentName: Optional[str] = Field(default=None,alias="documentName",)
	size: Optional[int] = Field(default=None,alias="size",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


