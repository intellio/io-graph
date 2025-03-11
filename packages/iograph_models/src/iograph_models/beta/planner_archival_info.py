from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerArchivalInfo(BaseModel):
	justification: Optional[str] = Field(alias="justification",default=None,)
	statusChangedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="statusChangedBy",default=None,)
	statusChangedDateTime: Optional[datetime] = Field(alias="statusChangedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

