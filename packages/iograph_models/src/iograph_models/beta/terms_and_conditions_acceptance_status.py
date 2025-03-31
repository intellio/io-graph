from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TermsAndConditionsAcceptanceStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termsAndConditionsAcceptanceStatus"] = Field(alias="@odata.type",)
	acceptedDateTime: Optional[datetime] = Field(alias="acceptedDateTime", default=None,)
	acceptedVersion: Optional[int] = Field(alias="acceptedVersion", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	termsAndConditions: Optional[TermsAndConditions] = Field(alias="termsAndConditions", default=None,)

from .terms_and_conditions import TermsAndConditions
