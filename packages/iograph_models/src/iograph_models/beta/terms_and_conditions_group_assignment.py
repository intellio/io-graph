from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TermsAndConditionsGroupAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termsAndConditionsGroupAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.termsAndConditionsGroupAssignment")
	targetGroupId: Optional[str] = Field(alias="targetGroupId", default=None,)
	termsAndConditions: Optional[TermsAndConditions] = Field(alias="termsAndConditions", default=None,)

from .terms_and_conditions import TermsAndConditions
