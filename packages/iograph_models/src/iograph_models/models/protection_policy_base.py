from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class ProtectionPolicyBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	retentionSettings: Optional[list[RetentionSetting]] = Field(default=None,alias="retentionSettings",)
	status: Optional[ProtectionPolicyStatus] = Field(default=None,alias="status",)

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

