from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TermsAndConditions(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	acceptanceStatement: Optional[str] = Field(default=None,alias="acceptanceStatement",)
	bodyText: Optional[str] = Field(default=None,alias="bodyText",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	title: Optional[str] = Field(default=None,alias="title",)
	version: Optional[int] = Field(default=None,alias="version",)
	acceptanceStatuses: Optional[list[TermsAndConditionsAcceptanceStatus]] = Field(default=None,alias="acceptanceStatuses",)
	assignments: Optional[list[TermsAndConditionsAssignment]] = Field(default=None,alias="assignments",)

from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
from .terms_and_conditions_assignment import TermsAndConditionsAssignment

