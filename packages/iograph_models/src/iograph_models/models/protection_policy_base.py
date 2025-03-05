from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectionPolicyBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings",default=None,)
	status: Optional[str | ProtectionPolicyStatus] = Field(alias="status",default=None,)

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
			if mapping_key == "#microsoft.graph.exchangeProtectionPolicy":
				from .exchange_protection_policy import ExchangeProtectionPolicy
				return ExchangeProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.oneDriveForBusinessProtectionPolicy":
				from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
				return OneDriveForBusinessProtectionPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointProtectionPolicy":
				from .share_point_protection_policy import SharePointProtectionPolicy
				return SharePointProtectionPolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus

