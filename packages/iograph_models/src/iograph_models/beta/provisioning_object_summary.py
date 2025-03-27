from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningObjectSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	action: Optional[str] = Field(alias="action", default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime", default=None,)
	changeId: Optional[str] = Field(alias="changeId", default=None,)
	cycleId: Optional[str] = Field(alias="cycleId", default=None,)
	durationInMilliseconds: Optional[int] = Field(alias="durationInMilliseconds", default=None,)
	initiatedBy: Optional[Initiator] = Field(alias="initiatedBy", default=None,)
	jobId: Optional[str] = Field(alias="jobId", default=None,)
	modifiedProperties: Optional[list[ModifiedProperty]] = Field(alias="modifiedProperties", default=None,)
	provisioningAction: Optional[ProvisioningAction | str] = Field(alias="provisioningAction", default=None,)
	provisioningStatusInfo: Optional[ProvisioningStatusInfo] = Field(alias="provisioningStatusInfo", default=None,)
	provisioningSteps: Optional[list[ProvisioningStep]] = Field(alias="provisioningSteps", default=None,)
	servicePrincipal: Optional[ProvisioningServicePrincipal] = Field(alias="servicePrincipal", default=None,)
	sourceIdentity: Optional[ProvisionedIdentity] = Field(alias="sourceIdentity", default=None,)
	sourceSystem: Optional[ProvisioningSystem] = Field(alias="sourceSystem", default=None,)
	statusInfo: Optional[Union[StatusDetails]] = Field(alias="statusInfo", default=None,discriminator="odata_type", )
	targetIdentity: Optional[ProvisionedIdentity] = Field(alias="targetIdentity", default=None,)
	targetSystem: Optional[ProvisioningSystem] = Field(alias="targetSystem", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

from .initiator import Initiator
from .modified_property import ModifiedProperty
from .provisioning_action import ProvisioningAction
from .provisioning_status_info import ProvisioningStatusInfo
from .provisioning_step import ProvisioningStep
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioned_identity import ProvisionedIdentity
from .provisioning_system import ProvisioningSystem
from .status_details import StatusDetails
from .provisioned_identity import ProvisionedIdentity
from .provisioning_system import ProvisioningSystem

