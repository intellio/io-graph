from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHealthIssue(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalInformation: Optional[list[str]] = Field(default=None,alias="additionalInformation",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainNames: Optional[list[str]] = Field(default=None,alias="domainNames",)
	healthIssueType: Optional[SecurityHealthIssueType] = Field(default=None,alias="healthIssueType",)
	issueTypeId: Optional[str] = Field(default=None,alias="issueTypeId",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	recommendations: Optional[list[str]] = Field(default=None,alias="recommendations",)
	recommendedActionCommands: Optional[list[str]] = Field(default=None,alias="recommendedActionCommands",)
	sensorDNSNames: Optional[list[str]] = Field(default=None,alias="sensorDNSNames",)
	severity: Optional[SecurityHealthIssueSeverity] = Field(default=None,alias="severity",)
	status: Optional[SecurityHealthIssueStatus] = Field(default=None,alias="status",)

from .security_health_issue_type import SecurityHealthIssueType
from .security_health_issue_severity import SecurityHealthIssueSeverity
from .security_health_issue_status import SecurityHealthIssueStatus

