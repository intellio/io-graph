from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedResource(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.networkaccess.relatedDestination":
				from .networkaccess_related_destination import NetworkaccessRelatedDestination
				return NetworkaccessRelatedDestination.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedDevice":
				from .networkaccess_related_device import NetworkaccessRelatedDevice
				return NetworkaccessRelatedDevice.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedFile":
				from .networkaccess_related_file import NetworkaccessRelatedFile
				return NetworkaccessRelatedFile.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedFileHash":
				from .networkaccess_related_file_hash import NetworkaccessRelatedFileHash
				return NetworkaccessRelatedFileHash.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedMalware":
				from .networkaccess_related_malware import NetworkaccessRelatedMalware
				return NetworkaccessRelatedMalware.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedRemoteNetwork":
				from .networkaccess_related_remote_network import NetworkaccessRelatedRemoteNetwork
				return NetworkaccessRelatedRemoteNetwork.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedTenant":
				from .networkaccess_related_tenant import NetworkaccessRelatedTenant
				return NetworkaccessRelatedTenant.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedThreatIntelligence":
				from .networkaccess_related_threat_intelligence import NetworkaccessRelatedThreatIntelligence
				return NetworkaccessRelatedThreatIntelligence.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedToken":
				from .networkaccess_related_token import NetworkaccessRelatedToken
				return NetworkaccessRelatedToken.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedTransaction":
				from .networkaccess_related_transaction import NetworkaccessRelatedTransaction
				return NetworkaccessRelatedTransaction.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedUrl":
				from .networkaccess_related_url import NetworkaccessRelatedUrl
				return NetworkaccessRelatedUrl.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedUser":
				from .networkaccess_related_user import NetworkaccessRelatedUser
				return NetworkaccessRelatedUser.model_validate(data)
			if mapping_key == "#microsoft.graph.networkaccess.relatedWebCategory":
				from .networkaccess_related_web_category import NetworkaccessRelatedWebCategory
				return NetworkaccessRelatedWebCategory.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


