from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHealthIssue(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalInformation: list[str] = Field(alias="additionalInformation",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainNames: list[Optional[str]] = Field(alias="domainNames",)
	healthIssueType: Optional[SecurityHealthIssueType] = Field(default=None,alias="healthIssueType",)
	issueTypeId: Optional[str] = Field(default=None,alias="issueTypeId",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	recommendations: list[str] = Field(alias="recommendations",)
	recommendedActionCommands: list[str] = Field(alias="recommendedActionCommands",)
	sensorDNSNames: list[Optional[str]] = Field(alias="sensorDNSNames",)
	severity: Optional[SecurityHealthIssueSeverity] = Field(default=None,alias="severity",)
	status: Optional[SecurityHealthIssueStatus] = Field(default=None,alias="status",)

from .security_health_issue_type import SecurityHealthIssueType
from .security_health_issue_severity import SecurityHealthIssueSeverity
from .security_health_issue_status import SecurityHealthIssueStatus

