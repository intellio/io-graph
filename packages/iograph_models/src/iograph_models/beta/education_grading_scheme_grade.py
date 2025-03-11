from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationGradingSchemeGrade(BaseModel):
	defaultPercentage: float | str | ReferenceNumeric
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	minPercentage: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

