from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySensor(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deploymentStatus: Optional[SecurityDeploymentStatus] = Field(default=None,alias="deploymentStatus",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	healthStatus: Optional[SecuritySensorHealthStatus] = Field(default=None,alias="healthStatus",)
	openHealthIssuesCount: Optional[int] = Field(default=None,alias="openHealthIssuesCount",)
	sensorType: Optional[SecuritySensorType] = Field(default=None,alias="sensorType",)
	settings: Optional[SecuritySensorSettings] = Field(default=None,alias="settings",)
	version: Optional[str] = Field(default=None,alias="version",)
	healthIssues: list[SecurityHealthIssue] = Field(alias="healthIssues",)

from .security_deployment_status import SecurityDeploymentStatus
from .security_sensor_health_status import SecuritySensorHealthStatus
from .security_sensor_type import SecuritySensorType
from .security_sensor_settings import SecuritySensorSettings
from .security_health_issue import SecurityHealthIssue

