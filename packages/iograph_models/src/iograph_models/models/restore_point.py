from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RestorePoint(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	protectionDateTime: Optional[datetime] = Field(alias="protectionDateTime",default=None,)
	tags: Optional[str | RestorePointTags] = Field(alias="tags",default=None,)
	protectionUnit: SerializeAsAny[Optional[ProtectionUnitBase]] = Field(alias="protectionUnit",default=None,)

from .restore_point_tags import RestorePointTags
from .protection_unit_base import ProtectionUnitBase

