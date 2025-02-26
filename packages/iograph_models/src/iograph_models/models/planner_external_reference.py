from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerExternalReference(BaseModel):
	alias: Optional[str] = Field(default=None,alias="alias",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	previewPriority: Optional[str] = Field(default=None,alias="previewPriority",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

