from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHealthIssue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.healthIssue"] = Field(alias="@odata.type",)
	additionalInformation: Optional[list[str]] = Field(alias="additionalInformation", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainNames: Optional[list[str]] = Field(alias="domainNames", default=None,)
	healthIssueType: Optional[SecurityHealthIssueType | str] = Field(alias="healthIssueType", default=None,)
	issueTypeId: Optional[str] = Field(alias="issueTypeId", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	recommendations: Optional[list[str]] = Field(alias="recommendations", default=None,)
	recommendedActionCommands: Optional[list[str]] = Field(alias="recommendedActionCommands", default=None,)
	sensorDNSNames: Optional[list[str]] = Field(alias="sensorDNSNames", default=None,)
	severity: Optional[SecurityHealthIssueSeverity | str] = Field(alias="severity", default=None,)
	status: Optional[SecurityHealthIssueStatus | str] = Field(alias="status", default=None,)

from .security_health_issue_type import SecurityHealthIssueType
from .security_health_issue_severity import SecurityHealthIssueSeverity
from .security_health_issue_status import SecurityHealthIssueStatus
