from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySensor(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deploymentStatus: Optional[SecurityDeploymentStatus | str] = Field(alias="deploymentStatus",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	domainName: Optional[str] = Field(alias="domainName",default=None,)
	healthStatus: Optional[SecuritySensorHealthStatus | str] = Field(alias="healthStatus",default=None,)
	openHealthIssuesCount: Optional[int] = Field(alias="openHealthIssuesCount",default=None,)
	sensorType: Optional[SecuritySensorType | str] = Field(alias="sensorType",default=None,)
	settings: Optional[SecuritySensorSettings] = Field(alias="settings",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	healthIssues: Optional[list[SecurityHealthIssue]] = Field(alias="healthIssues",default=None,)

from .security_deployment_status import SecurityDeploymentStatus
from .security_sensor_health_status import SecuritySensorHealthStatus
from .security_sensor_type import SecuritySensorType
from .security_sensor_settings import SecuritySensorSettings
from .security_health_issue import SecurityHealthIssue

