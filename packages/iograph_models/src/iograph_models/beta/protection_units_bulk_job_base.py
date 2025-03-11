from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectionUnitsBulkJobBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[ProtectionUnitsBulkJobStatus | str] = Field(alias="status",default=None,)

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
			if mapping_key == "#microsoft.graph.driveProtectionUnitsBulkAdditionJob":
				from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
				return DriveProtectionUnitsBulkAdditionJob.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxProtectionUnitsBulkAdditionJob":
				from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
				return MailboxProtectionUnitsBulkAdditionJob.model_validate(data)
			if mapping_key == "#microsoft.graph.siteProtectionUnitsBulkAdditionJob":
				from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob
				return SiteProtectionUnitsBulkAdditionJob.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_units_bulk_job_status import ProtectionUnitsBulkJobStatus

