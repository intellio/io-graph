from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermsAndConditionsGroupAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	targetGroupId: Optional[str] = Field(alias="targetGroupId",default=None,)
	termsAndConditions: Optional[TermsAndConditions] = Field(alias="termsAndConditions",default=None,)

from .terms_and_conditions import TermsAndConditions

