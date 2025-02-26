from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationOutcomeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EducationOutcome] = Field(alias="value",)

from .education_outcome import EducationOutcome

