from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MembershipRuleProcessingStatus(BaseModel):
	errorMessage: Optional[str] = Field(alias="errorMessage",default=None,)
	lastMembershipUpdated: Optional[datetime] = Field(alias="lastMembershipUpdated",default=None,)
	status: Optional[MembershipRuleProcessingStatusDetails | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .membership_rule_processing_status_details import MembershipRuleProcessingStatusDetails

