from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityExportFileMetadata(BaseModel):
	downloadUrl: Optional[str] = Field(alias="downloadUrl", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


