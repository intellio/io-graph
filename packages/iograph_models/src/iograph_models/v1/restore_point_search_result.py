from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePointSearchResult(BaseModel):
	artifactHitCount: Optional[int] = Field(alias="artifactHitCount",default=None,)
	restorePoint: Optional[RestorePoint] = Field(alias="restorePoint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .restore_point import RestorePoint

