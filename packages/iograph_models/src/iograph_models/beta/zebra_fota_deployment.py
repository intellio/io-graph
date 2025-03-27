from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ZebraFotaDeployment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deploymentAssignments: Optional[list[AndroidFotaDeploymentAssignment]] = Field(alias="deploymentAssignments", default=None,)
	deploymentSettings: Optional[ZebraFotaDeploymentSettings] = Field(alias="deploymentSettings", default=None,)
	deploymentStatus: Optional[ZebraFotaDeploymentStatus] = Field(alias="deploymentStatus", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)

from .android_fota_deployment_assignment import AndroidFotaDeploymentAssignment
from .zebra_fota_deployment_settings import ZebraFotaDeploymentSettings
from .zebra_fota_deployment_status import ZebraFotaDeploymentStatus

