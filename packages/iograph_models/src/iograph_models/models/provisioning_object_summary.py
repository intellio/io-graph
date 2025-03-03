from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ProvisioningObjectSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	changeId: Optional[str] = Field(default=None,alias="changeId",)
	cycleId: Optional[str] = Field(default=None,alias="cycleId",)
	durationInMilliseconds: Optional[int] = Field(default=None,alias="durationInMilliseconds",)
	initiatedBy: Optional[Initiator] = Field(default=None,alias="initiatedBy",)
	jobId: Optional[str] = Field(default=None,alias="jobId",)
	modifiedProperties: Optional[list[ModifiedProperty]] = Field(default=None,alias="modifiedProperties",)
	provisioningAction: Optional[ProvisioningAction] = Field(default=None,alias="provisioningAction",)
	provisioningStatusInfo: Optional[ProvisioningStatusInfo] = Field(default=None,alias="provisioningStatusInfo",)
	provisioningSteps: Optional[list[ProvisioningStep]] = Field(default=None,alias="provisioningSteps",)
	servicePrincipal: Optional[ProvisioningServicePrincipal] = Field(default=None,alias="servicePrincipal",)
	sourceIdentity: Optional[ProvisionedIdentity] = Field(default=None,alias="sourceIdentity",)
	sourceSystem: Optional[ProvisioningSystem] = Field(default=None,alias="sourceSystem",)
	targetIdentity: Optional[ProvisionedIdentity] = Field(default=None,alias="targetIdentity",)
	targetSystem: Optional[ProvisioningSystem] = Field(default=None,alias="targetSystem",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)

from .initiator import Initiator
from .modified_property import ModifiedProperty
from .provisioning_action import ProvisioningAction
from .provisioning_status_info import ProvisioningStatusInfo
from .provisioning_step import ProvisioningStep
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioned_identity import ProvisionedIdentity
from .provisioning_system import ProvisioningSystem
from .provisioned_identity import ProvisionedIdentity
from .provisioning_system import ProvisioningSystem

