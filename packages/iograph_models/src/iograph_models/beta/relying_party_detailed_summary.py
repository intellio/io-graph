from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RelyingPartyDetailedSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.relyingPartyDetailedSummary"] = Field(alias="@odata.type", default="#microsoft.graph.relyingPartyDetailedSummary")
	failedSignInCount: Optional[int] = Field(alias="failedSignInCount", default=None,)
	migrationStatus: Optional[MigrationStatus | str] = Field(alias="migrationStatus", default=None,)
	migrationValidationDetails: Optional[list[KeyValuePair]] = Field(alias="migrationValidationDetails", default=None,)
	relyingPartyId: Optional[str] = Field(alias="relyingPartyId", default=None,)
	relyingPartyName: Optional[str] = Field(alias="relyingPartyName", default=None,)
	replyUrls: Optional[list[str]] = Field(alias="replyUrls", default=None,)
	serviceId: Optional[str] = Field(alias="serviceId", default=None,)
	signInSuccessRate: float | str | ReferenceNumeric
	successfulSignInCount: Optional[int] = Field(alias="successfulSignInCount", default=None,)
	totalSignInCount: Optional[int] = Field(alias="totalSignInCount", default=None,)
	uniqueUserCount: Optional[int] = Field(alias="uniqueUserCount", default=None,)

from .migration_status import MigrationStatus
from .key_value_pair import KeyValuePair
from .reference_numeric import ReferenceNumeric
