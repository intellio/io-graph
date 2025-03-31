from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EducationAssignment]] = Field(alias="value", default=None,)

from .education_assignment import EducationAssignment
