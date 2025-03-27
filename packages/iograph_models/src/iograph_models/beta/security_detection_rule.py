from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDetectionRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.detectionRule"] = Field(alias="@odata.type", default="#microsoft.graph.security.detectionRule")
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	detectionAction: Optional[SecurityDetectionAction] = Field(alias="detectionAction", default=None,)
	detectorId: Optional[str] = Field(alias="detectorId", default=None,)
	lastRunDetails: Optional[SecurityRunDetails] = Field(alias="lastRunDetails", default=None,)
	queryCondition: Optional[SecurityQueryCondition] = Field(alias="queryCondition", default=None,)
	schedule: Optional[SecurityRuleSchedule] = Field(alias="schedule", default=None,)

from .security_detection_action import SecurityDetectionAction
from .security_run_details import SecurityRunDetails
from .security_query_condition import SecurityQueryCondition
from .security_rule_schedule import SecurityRuleSchedule

