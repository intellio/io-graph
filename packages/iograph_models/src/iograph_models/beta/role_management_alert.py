from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class RoleManagementAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.roleManagementAlert"] = Field(alias="@odata.type", default="#microsoft.graph.roleManagementAlert")
	alertConfigurations: Optional[list[Annotated[Union[InvalidLicenseAlertConfiguration, NoMfaOnRoleActivationAlertConfiguration, RedundantAssignmentAlertConfiguration, RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration, SequentialActivationRenewalsAlertConfiguration, StaleSignInAlertConfiguration, TooManyGlobalAdminsAssignedToTenantAlertConfiguration],Field(discriminator="odata_type")]]] = Field(alias="alertConfigurations", default=None,)
	alertDefinitions: Optional[list[UnifiedRoleManagementAlertDefinition]] = Field(alias="alertDefinitions", default=None,)
	alerts: Optional[list[UnifiedRoleManagementAlert]] = Field(alias="alerts", default=None,)
	operations: Optional[list[Annotated[Union[AttackSimulationOperation, EngagementAsyncOperation, GoalsExportJob, RichLongRunningOperation, IndustryDataFileValidateOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)

from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
from .unified_role_management_alert import UnifiedRoleManagementAlert
from .attack_simulation_operation import AttackSimulationOperation
from .engagement_async_operation import EngagementAsyncOperation
from .goals_export_job import GoalsExportJob
from .rich_long_running_operation import RichLongRunningOperation
from .industry_data_file_validate_operation import IndustryDataFileValidateOperation
