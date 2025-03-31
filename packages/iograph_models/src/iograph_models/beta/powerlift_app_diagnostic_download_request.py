from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PowerliftAppDiagnosticDownloadRequest(BaseModel):
	files: Optional[list[str]] = Field(alias="files", default=None,)
	powerliftId: Optional[str] = Field(alias="powerliftId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

