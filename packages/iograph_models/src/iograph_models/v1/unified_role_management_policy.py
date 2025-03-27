from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isOrganizationDefault: Optional[bool] = Field(alias="isOrganizationDefault", default=None,)
	lastModifiedBy: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, UserIdentity, CallRecordsUserIdentity]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	scopeId: Optional[str] = Field(alias="scopeId", default=None,)
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	effectiveRules: Optional[list[Annotated[Union[UnifiedRoleManagementPolicyApprovalRule, UnifiedRoleManagementPolicyAuthenticationContextRule, UnifiedRoleManagementPolicyEnablementRule, UnifiedRoleManagementPolicyExpirationRule, UnifiedRoleManagementPolicyNotificationRule],Field(discriminator="odata_type")]]] = Field(alias="effectiveRules", default=None,)
	rules: Optional[list[Annotated[Union[UnifiedRoleManagementPolicyApprovalRule, UnifiedRoleManagementPolicyAuthenticationContextRule, UnifiedRoleManagementPolicyEnablementRule, UnifiedRoleManagementPolicyExpirationRule, UnifiedRoleManagementPolicyNotificationRule],Field(discriminator="odata_type")]]] = Field(alias="rules", default=None,)

from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
from .communications_application_identity import CommunicationsApplicationIdentity
from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
from .communications_encrypted_identity import CommunicationsEncryptedIdentity
from .communications_guest_identity import CommunicationsGuestIdentity
from .communications_phone_identity import CommunicationsPhoneIdentity
from .communications_user_identity import CommunicationsUserIdentity
from .email_identity import EmailIdentity
from .initiator import Initiator
from .provisioned_identity import ProvisionedIdentity
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioning_system import ProvisioningSystem
from .service_principal_identity import ServicePrincipalIdentity
from .share_point_identity import SharePointIdentity
from .teamwork_application_identity import TeamworkApplicationIdentity
from .teamwork_conversation_identity import TeamworkConversationIdentity
from .teamwork_tag_identity import TeamworkTagIdentity
from .teamwork_user_identity import TeamworkUserIdentity
from .user_identity import UserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

