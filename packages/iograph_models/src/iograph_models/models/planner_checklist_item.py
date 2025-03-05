from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerChecklistItem(BaseModel):
	isChecked: Optional[bool] = Field(default=None,alias="isChecked",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	orderHint: Optional[str] = Field(default=None,alias="orderHint",)
	title: Optional[str] = Field(default=None,alias="title",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

