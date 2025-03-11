from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSetContent(BaseModel):
	contentType: Optional[ContentTypeInfo] = Field(alias="contentType",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)
	folderName: Optional[str] = Field(alias="folderName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .content_type_info import ContentTypeInfo

