from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RelyingPartyDetailedSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	failedSignInCount: Optional[int] = Field(default=None,alias="failedSignInCount",)
	migrationStatus: Optional[MigrationStatus] = Field(default=None,alias="migrationStatus",)
	migrationValidationDetails: list[KeyValuePair] = Field(alias="migrationValidationDetails",)
	relyingPartyId: Optional[str] = Field(default=None,alias="relyingPartyId",)
	relyingPartyName: Optional[str] = Field(default=None,alias="relyingPartyName",)
	replyUrls: list[str] = Field(alias="replyUrls",)
	serviceId: Optional[str] = Field(default=None,alias="serviceId",)
	signInSuccessRate: Optional[float] | Optional[str] | ReferenceNumeric
	successfulSignInCount: Optional[int] = Field(default=None,alias="successfulSignInCount",)
	totalSignInCount: Optional[int] = Field(default=None,alias="totalSignInCount",)
	uniqueUserCount: Optional[int] = Field(default=None,alias="uniqueUserCount",)

from .migration_status import MigrationStatus
from .key_value_pair import KeyValuePair
from .reference_numeric import ReferenceNumeric

