from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class HardwareOathTokenAuthenticationMethodDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice"] = Field(alias="@odata.type", default="#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hardwareOathDevices: Optional[list[HardwareOathTokenAuthenticationMethodDevice]] = Field(alias="hardwareOathDevices", default=None,)
	assignedTo: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProgramResource, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, SourceProvisionedIdentity, TargetProvisionedIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, AuditUserIdentity, CallRecordsUserIdentity, SecuritySubmissionUserIdentity]] = Field(alias="assignedTo", default=None,discriminator="odata_type", )
	hashFunction: Optional[HardwareOathTokenHashFunction | str] = Field(alias="hashFunction", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	secretKey: Optional[str] = Field(alias="secretKey", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	status: Optional[HardwareOathTokenStatus | str] = Field(alias="status", default=None,)
	timeIntervalInSeconds: Optional[int] = Field(alias="timeIntervalInSeconds", default=None,)
	assignTo: Optional[User] = Field(alias="assignTo", default=None,)

from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
from .communications_application_identity import CommunicationsApplicationIdentity
from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
from .communications_encrypted_identity import CommunicationsEncryptedIdentity
from .communications_guest_identity import CommunicationsGuestIdentity
from .communications_phone_identity import CommunicationsPhoneIdentity
from .communications_user_identity import CommunicationsUserIdentity
from .email_identity import EmailIdentity
from .initiator import Initiator
from .program_resource import ProgramResource
from .provisioned_identity import ProvisionedIdentity
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioning_system import ProvisioningSystem
from .service_principal_identity import ServicePrincipalIdentity
from .share_point_identity import SharePointIdentity
from .source_provisioned_identity import SourceProvisionedIdentity
from .target_provisioned_identity import TargetProvisionedIdentity
from .teamwork_application_identity import TeamworkApplicationIdentity
from .teamwork_conversation_identity import TeamworkConversationIdentity
from .teamwork_tag_identity import TeamworkTagIdentity
from .teamwork_user_identity import TeamworkUserIdentity
from .audit_user_identity import AuditUserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .security_submission_user_identity import SecuritySubmissionUserIdentity
from .hardware_oath_token_hash_function import HardwareOathTokenHashFunction
from .hardware_oath_token_status import HardwareOathTokenStatus
from .user import User
