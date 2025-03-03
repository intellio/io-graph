from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermsAndConditionsAcceptanceStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TermsAndConditionsAcceptanceStatus]] = Field(default=None,alias="value",)

from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus

