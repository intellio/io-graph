from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	protectionDateTime: Optional[datetime] = Field(default=None,alias="protectionDateTime",)
	tags: Optional[RestorePointTags] = Field(default=None,alias="tags",)
	protectionUnit: Optional[ProtectionUnitBase] = Field(default=None,alias="protectionUnit",)

from .restore_point_tags import RestorePointTags
from .protection_unit_base import ProtectionUnitBase

