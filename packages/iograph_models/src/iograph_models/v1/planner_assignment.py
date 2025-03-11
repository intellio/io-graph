from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerAssignment(BaseModel):
	assignedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="assignedBy",default=None,)
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime",default=None,)
	orderHint: Optional[str] = Field(alias="orderHint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

