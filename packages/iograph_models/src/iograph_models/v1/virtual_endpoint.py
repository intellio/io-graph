from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class VirtualEndpoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEndpoint")
	auditEvents: Optional[list[CloudPcAuditEvent]] = Field(alias="auditEvents", default=None,)
	cloudPCs: Optional[list[CloudPC]] = Field(alias="cloudPCs", default=None,)
	deviceImages: Optional[list[CloudPcDeviceImage]] = Field(alias="deviceImages", default=None,)
	galleryImages: Optional[list[CloudPcGalleryImage]] = Field(alias="galleryImages", default=None,)
	onPremisesConnections: Optional[list[CloudPcOnPremisesConnection]] = Field(alias="onPremisesConnections", default=None,)
	provisioningPolicies: Optional[list[CloudPcProvisioningPolicy]] = Field(alias="provisioningPolicies", default=None,)
	userSettings: Optional[list[CloudPcUserSetting]] = Field(alias="userSettings", default=None,)

from .cloud_pc_audit_event import CloudPcAuditEvent
from .cloud_p_c import CloudPC
from .cloud_pc_device_image import CloudPcDeviceImage
from .cloud_pc_gallery_image import CloudPcGalleryImage
from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
from .cloud_pc_user_setting import CloudPcUserSetting
