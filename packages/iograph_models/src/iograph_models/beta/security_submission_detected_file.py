from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySubmissionDetectedFile(BaseModel):
	fileHash: Optional[str] = Field(alias="fileHash", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

