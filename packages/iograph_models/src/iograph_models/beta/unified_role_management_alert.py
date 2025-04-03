from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class UnifiedRoleManagementAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementAlert"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementAlert")
	alertDefinitionId: Optional[str] = Field(alias="alertDefinitionId", default=None,)
	incidentCount: Optional[int] = Field(alias="incidentCount", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastScannedDateTime: Optional[datetime] = Field(alias="lastScannedDateTime", default=None,)
	scopeId: Optional[str] = Field(alias="scopeId", default=None,)
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	alertConfiguration: Optional[Union[InvalidLicenseAlertConfiguration, NoMfaOnRoleActivationAlertConfiguration, RedundantAssignmentAlertConfiguration, RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration, SequentialActivationRenewalsAlertConfiguration, StaleSignInAlertConfiguration, TooManyGlobalAdminsAssignedToTenantAlertConfiguration]] = Field(alias="alertConfiguration", default=None,discriminator="odata_type", )
	alertDefinition: Optional[UnifiedRoleManagementAlertDefinition] = Field(alias="alertDefinition", default=None,)
	alertIncidents: Optional[list[Annotated[Union[InvalidLicenseAlertIncident, NoMfaOnRoleActivationAlertIncident, RedundantAssignmentAlertIncident, RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident, SequentialActivationRenewalsAlertIncident, StaleSignInAlertIncident, TooManyGlobalAdminsAssignedToTenantAlertIncident],Field(discriminator="odata_type")]]] = Field(alias="alertIncidents", default=None,)

from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
from .invalid_license_alert_incident import InvalidLicenseAlertIncident
from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
from .stale_sign_in_alert_incident import StaleSignInAlertIncident
from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
