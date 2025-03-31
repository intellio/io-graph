from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestoreSessionArtifactCount(BaseModel):
	completed: Optional[int] = Field(alias="completed", default=None,)
	failed: Optional[int] = Field(alias="failed", default=None,)
	inProgress: Optional[int] = Field(alias="inProgress", default=None,)
	total: Optional[int] = Field(alias="total", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

