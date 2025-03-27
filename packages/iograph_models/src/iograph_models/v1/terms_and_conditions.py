from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TermsAndConditions(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	acceptanceStatement: Optional[str] = Field(alias="acceptanceStatement", default=None,)
	bodyText: Optional[str] = Field(alias="bodyText", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	acceptanceStatuses: Optional[list[TermsAndConditionsAcceptanceStatus]] = Field(alias="acceptanceStatuses", default=None,)
	assignments: Optional[list[TermsAndConditionsAssignment]] = Field(alias="assignments", default=None,)

from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
from .terms_and_conditions_assignment import TermsAndConditionsAssignment

