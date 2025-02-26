from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class ProtectionUnitBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	policyId: Optional[str] = Field(default=None,alias="policyId",)
	status: Optional[ProtectionUnitStatus] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.driveProtectionUnit":
				from .drive_protection_unit import DriveProtectionUnit
				return DriveProtectionUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionUnit":
				from .mailbox_protection_unit import MailboxProtectionUnit
				return MailboxProtectionUnit.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionUnit":
				from .site_protection_unit import SiteProtectionUnit
				return SiteProtectionUnit.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_unit_status import ProtectionUnitStatus

