from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class PowerliftDownloadRequest(BaseModel):
	files: Optional[list[str]] = Field(alias="files", default=None,)
	powerliftId: Optional[UUID] = Field(alias="powerliftId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

