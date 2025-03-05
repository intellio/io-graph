from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentPointsGrade(BaseModel):
	gradedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="gradedBy",)
	gradedDateTime: Optional[datetime] = Field(default=None,alias="gradedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	points: float | str | ReferenceNumeric

from .identity_set import IdentitySet
from .reference_numeric import ReferenceNumeric

