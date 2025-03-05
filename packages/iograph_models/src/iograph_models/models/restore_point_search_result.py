from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePointSearchResult(BaseModel):
	artifactHitCount: Optional[int] = Field(default=None,alias="artifactHitCount",)
	restorePoint: Optional[RestorePoint] = Field(default=None,alias="restorePoint",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .restore_point import RestorePoint

