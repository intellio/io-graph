from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TermsAndConditionsAcceptanceStatus(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	acceptedDateTime: Optional[datetime] = Field(default=None,alias="acceptedDateTime",)
	acceptedVersion: Optional[int] = Field(default=None,alias="acceptedVersion",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	termsAndConditions: Optional[TermsAndConditions] = Field(default=None,alias="termsAndConditions",)

from .terms_and_conditions import TermsAndConditions

