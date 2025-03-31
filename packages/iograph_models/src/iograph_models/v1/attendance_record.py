from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class AttendanceRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.attendanceRecord"] = Field(alias="@odata.type",)
	attendanceIntervals: Optional[list[AttendanceInterval]] = Field(alias="attendanceIntervals", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	identity: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, UserIdentity, CallRecordsUserIdentity]] = Field(alias="identity", default=None,discriminator="odata_type", )
	role: Optional[str] = Field(alias="role", default=None,)
	totalAttendanceInSeconds: Optional[int] = Field(alias="totalAttendanceInSeconds", default=None,)

from .attendance_interval import AttendanceInterval
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
