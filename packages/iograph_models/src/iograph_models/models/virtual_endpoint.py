from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEndpoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	auditEvents: Optional[list[CloudPcAuditEvent]] = Field(default=None,alias="auditEvents",)
	cloudPCs: Optional[list[CloudPC]] = Field(default=None,alias="cloudPCs",)
	deviceImages: Optional[list[CloudPcDeviceImage]] = Field(default=None,alias="deviceImages",)
	galleryImages: Optional[list[CloudPcGalleryImage]] = Field(default=None,alias="galleryImages",)
	onPremisesConnections: Optional[list[CloudPcOnPremisesConnection]] = Field(default=None,alias="onPremisesConnections",)
	provisioningPolicies: Optional[list[CloudPcProvisioningPolicy]] = Field(default=None,alias="provisioningPolicies",)
	userSettings: Optional[list[CloudPcUserSetting]] = Field(default=None,alias="userSettings",)

from .cloud_pc_audit_event import CloudPcAuditEvent
from .cloud_p_c import CloudPC
from .cloud_pc_device_image import CloudPcDeviceImage
from .cloud_pc_gallery_image import CloudPcGalleryImage
from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
from .cloud_pc_user_setting import CloudPcUserSetting

