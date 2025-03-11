from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ContentProperties(BaseModel):
	extensions: Optional[list[str]] = Field(alias="extensions",default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	metadata: Optional[ContentMetadata] = Field(alias="metadata",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .content_metadata import ContentMetadata

