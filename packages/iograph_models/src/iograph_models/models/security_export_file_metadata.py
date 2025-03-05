from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityExportFileMetadata(BaseModel):
	downloadUrl: Optional[str] = Field(default=None,alias="downloadUrl",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	size: Optional[int] = Field(default=None,alias="size",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


