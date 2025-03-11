from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentPointsGrade(BaseModel):
	gradedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="gradedBy",default=None,)
	gradedDateTime: Optional[datetime] = Field(alias="gradedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	points: float | str | ReferenceNumeric

from .identity_set import IdentitySet
from .reference_numeric import ReferenceNumeric

