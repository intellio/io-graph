from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class SharingLink(BaseModel):
	application: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProgramResource, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, SourceProvisionedIdentity, TargetProvisionedIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, AuditUserIdentity, CallRecordsUserIdentity, SecuritySubmissionUserIdentity]] = Field(alias="application", default=None,discriminator="odata_type", )
	configuratorUrl: Optional[str] = Field(alias="configuratorUrl", default=None,)
	preventsDownload: Optional[bool] = Field(alias="preventsDownload", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	webHtml: Optional[str] = Field(alias="webHtml", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
