from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[InvalidLicenseAlertIncident, NoMfaOnRoleActivationAlertIncident, RedundantAssignmentAlertIncident, RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident, SequentialActivationRenewalsAlertIncident, StaleSignInAlertIncident, TooManyGlobalAdminsAssignedToTenantAlertIncident]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .invalid_license_alert_incident import InvalidLicenseAlertIncident
from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
from .stale_sign_in_alert_incident import StaleSignInAlertIncident
from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

