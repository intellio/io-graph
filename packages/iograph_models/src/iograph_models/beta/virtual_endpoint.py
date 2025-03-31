from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class VirtualEndpoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEndpoint"] = Field(alias="@odata.type",)
	auditEvents: Optional[list[CloudPcAuditEvent]] = Field(alias="auditEvents", default=None,)
	bulkActions: Optional[list[Annotated[Union[CloudPcBulkCreateSnapshot, CloudPcBulkDisasterRecoveryFailback, CloudPcBulkDisasterRecoveryFailover, CloudPcBulkModifyDiskEncryptionType, CloudPcBulkMove, CloudPcBulkPowerOff, CloudPcBulkPowerOn, CloudPcBulkReprovision, CloudPcBulkResize, CloudPcBulkRestart, CloudPcBulkRestore, CloudPcBulkSetReviewStatus, CloudPcBulkTroubleshoot],Field(discriminator="odata_type")]]] = Field(alias="bulkActions", default=None,)
	cloudPCs: Optional[list[CloudPC]] = Field(alias="cloudPCs", default=None,)
	crossCloudGovernmentOrganizationMapping: Optional[CloudPcCrossCloudGovernmentOrganizationMapping] = Field(alias="crossCloudGovernmentOrganizationMapping", default=None,)
	deviceImages: Optional[list[CloudPcDeviceImage]] = Field(alias="deviceImages", default=None,)
	externalPartnerSettings: Optional[list[CloudPcExternalPartnerSetting]] = Field(alias="externalPartnerSettings", default=None,)
	frontLineServicePlans: Optional[list[CloudPcFrontLineServicePlan]] = Field(alias="frontLineServicePlans", default=None,)
	galleryImages: Optional[list[CloudPcGalleryImage]] = Field(alias="galleryImages", default=None,)
	onPremisesConnections: Optional[list[CloudPcOnPremisesConnection]] = Field(alias="onPremisesConnections", default=None,)
	organizationSettings: Optional[CloudPcOrganizationSettings] = Field(alias="organizationSettings", default=None,)
	provisioningPolicies: Optional[list[CloudPcProvisioningPolicy]] = Field(alias="provisioningPolicies", default=None,)
	reports: Optional[CloudPcReports] = Field(alias="reports", default=None,)
	servicePlans: Optional[list[CloudPcServicePlan]] = Field(alias="servicePlans", default=None,)
	snapshots: Optional[list[CloudPcSnapshot]] = Field(alias="snapshots", default=None,)
	supportedRegions: Optional[list[CloudPcSupportedRegion]] = Field(alias="supportedRegions", default=None,)
	userSettings: Optional[list[CloudPcUserSetting]] = Field(alias="userSettings", default=None,)

from .cloud_pc_audit_event import CloudPcAuditEvent
from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
from .cloud_pc_bulk_move import CloudPcBulkMove
from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
from .cloud_pc_bulk_resize import CloudPcBulkResize
from .cloud_pc_bulk_restart import CloudPcBulkRestart
from .cloud_pc_bulk_restore import CloudPcBulkRestore
from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
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
