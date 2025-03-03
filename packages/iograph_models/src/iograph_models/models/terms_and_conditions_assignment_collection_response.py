from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermsAndConditionsAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TermsAndConditionsAssignment]] = Field(default=None,alias="value",)

from .terms_and_conditions_assignment import TermsAndConditionsAssignment

