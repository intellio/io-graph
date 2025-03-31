from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermsAndConditionsAcceptanceStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TermsAndConditionsAcceptanceStatus]] = Field(alias="value", default=None,)

from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
