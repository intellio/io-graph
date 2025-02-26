from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class Identity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.azureCommunicationServicesUserIdentity":
				from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
				return AzureCommunicationServicesUserIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsApplicationIdentity":
				from .communications_application_identity import CommunicationsApplicationIdentity
				return CommunicationsApplicationIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsApplicationInstanceIdentity":
				from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
				return CommunicationsApplicationInstanceIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsEncryptedIdentity":
				from .communications_encrypted_identity import CommunicationsEncryptedIdentity
				return CommunicationsEncryptedIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsGuestIdentity":
				from .communications_guest_identity import CommunicationsGuestIdentity
				return CommunicationsGuestIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsPhoneIdentity":
				from .communications_phone_identity import CommunicationsPhoneIdentity
				return CommunicationsPhoneIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsUserIdentity":
				from .communications_user_identity import CommunicationsUserIdentity
				return CommunicationsUserIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.emailIdentity":
				from .email_identity import EmailIdentity
				return EmailIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.initiator":
				from .initiator import Initiator
				return Initiator.model_validate(data)
			if mapping_key == "#microsoft.graph.provisionedIdentity":
				from .provisioned_identity import ProvisionedIdentity
				return ProvisionedIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.provisioningServicePrincipal":
				from .provisioning_service_principal import ProvisioningServicePrincipal
				return ProvisioningServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.provisioningSystem":
				from .provisioning_system import ProvisioningSystem
				return ProvisioningSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.servicePrincipalIdentity":
				from .service_principal_identity import ServicePrincipalIdentity
				return ServicePrincipalIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointIdentity":
				from .share_point_identity import SharePointIdentity
				return SharePointIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkApplicationIdentity":
				from .teamwork_application_identity import TeamworkApplicationIdentity
				return TeamworkApplicationIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkConversationIdentity":
				from .teamwork_conversation_identity import TeamworkConversationIdentity
				return TeamworkConversationIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkTagIdentity":
				from .teamwork_tag_identity import TeamworkTagIdentity
				return TeamworkTagIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.teamworkUserIdentity":
				from .teamwork_user_identity import TeamworkUserIdentity
				return TeamworkUserIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.userIdentity":
				from .user_identity import UserIdentity
				return UserIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.userIdentity":
				from .call_records_user_identity import CallRecordsUserIdentity
				return CallRecordsUserIdentity.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


