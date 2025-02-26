from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DocumentSetContent(BaseModel):
	contentType: Optional[ContentTypeInfo] = Field(default=None,alias="contentType",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	folderName: Optional[str] = Field(default=None,alias="folderName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .content_type_info import ContentTypeInfo

