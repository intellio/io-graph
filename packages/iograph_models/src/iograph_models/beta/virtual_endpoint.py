from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEndpoint(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	auditEvents: Optional[list[CloudPcAuditEvent]] = Field(alias="auditEvents",default=None,)
	bulkActions: SerializeAsAny[Optional[list[CloudPcBulkAction]]] = Field(alias="bulkActions",default=None,)
	cloudPCs: Optional[list[CloudPC]] = Field(alias="cloudPCs",default=None,)
	crossCloudGovernmentOrganizationMapping: Optional[CloudPcCrossCloudGovernmentOrganizationMapping] = Field(alias="crossCloudGovernmentOrganizationMapping",default=None,)
	deviceImages: Optional[list[CloudPcDeviceImage]] = Field(alias="deviceImages",default=None,)
	externalPartnerSettings: Optional[list[CloudPcExternalPartnerSetting]] = Field(alias="externalPartnerSettings",default=None,)
	frontLineServicePlans: Optional[list[CloudPcFrontLineServicePlan]] = Field(alias="frontLineServicePlans",default=None,)
	galleryImages: Optional[list[CloudPcGalleryImage]] = Field(alias="galleryImages",default=None,)
	onPremisesConnections: Optional[list[CloudPcOnPremisesConnection]] = Field(alias="onPremisesConnections",default=None,)
	organizationSettings: Optional[CloudPcOrganizationSettings] = Field(alias="organizationSettings",default=None,)
	provisioningPolicies: Optional[list[CloudPcProvisioningPolicy]] = Field(alias="provisioningPolicies",default=None,)
	reports: Optional[CloudPcReports] = Field(alias="reports",default=None,)
	servicePlans: Optional[list[CloudPcServicePlan]] = Field(alias="servicePlans",default=None,)
	snapshots: Optional[list[CloudPcSnapshot]] = Field(alias="snapshots",default=None,)
	supportedRegions: Optional[list[CloudPcSupportedRegion]] = Field(alias="supportedRegions",default=None,)
	userSettings: Optional[list[CloudPcUserSetting]] = Field(alias="userSettings",default=None,)

from .cloud_pc_audit_event import CloudPcAuditEvent
from .cloud_pc_bulk_action import CloudPcBulkAction
from .cloud_p_c import CloudPC
from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
from .cloud_pc_device_image import CloudPcDeviceImage
from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
from .cloud_pc_gallery_image import CloudPcGalleryImage
from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
from .cloud_pc_organization_settings import CloudPcOrganizationSettings
from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
from .cloud_pc_reports import CloudPcReports
from .cloud_pc_service_plan import CloudPcServicePlan
from .cloud_pc_snapshot import CloudPcSnapshot
from .cloud_pc_supported_region import CloudPcSupportedRegion
from .cloud_pc_user_setting import CloudPcUserSetting

