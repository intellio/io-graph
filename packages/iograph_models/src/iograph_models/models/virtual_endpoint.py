from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEndpoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	auditEvents: list[CloudPcAuditEvent] = Field(alias="auditEvents",)
	cloudPCs: list[CloudPC] = Field(alias="cloudPCs",)
	deviceImages: list[CloudPcDeviceImage] = Field(alias="deviceImages",)
	galleryImages: list[CloudPcGalleryImage] = Field(alias="galleryImages",)
	onPremisesConnections: list[CloudPcOnPremisesConnection] = Field(alias="onPremisesConnections",)
	provisioningPolicies: list[CloudPcProvisioningPolicy] = Field(alias="provisioningPolicies",)
	userSettings: list[CloudPcUserSetting] = Field(alias="userSettings",)

from .cloud_pc_audit_event import CloudPcAuditEvent
from .cloud_p_c import CloudPC
from .cloud_pc_device_image import CloudPcDeviceImage
from .cloud_pc_gallery_image import CloudPcGalleryImage
from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
from .cloud_pc_user_setting import CloudPcUserSetting

