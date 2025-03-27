from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRunDetails(BaseModel):
	errorCode: Optional[SecurityHuntingRuleErrorCode | str] = Field(alias="errorCode", default=None,)
	failureReason: Optional[str] = Field(alias="failureReason", default=None,)
	lastRunDateTime: Optional[datetime] = Field(alias="lastRunDateTime", default=None,)
	status: Optional[SecurityHuntingRuleRunStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_hunting_rule_error_code import SecurityHuntingRuleErrorCode
from .security_hunting_rule_run_status import SecurityHuntingRuleRunStatus

