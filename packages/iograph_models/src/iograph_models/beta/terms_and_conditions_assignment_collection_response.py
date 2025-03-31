from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermsAndConditionsAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TermsAndConditionsAssignment]] = Field(alias="value", default=None,)

from .terms_and_conditions_assignment import TermsAndConditionsAssignment
