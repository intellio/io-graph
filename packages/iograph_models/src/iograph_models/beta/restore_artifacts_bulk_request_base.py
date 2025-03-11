from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RestoreArtifactsBulkRequestBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	destinationType: Optional[DestinationType | str] = Field(alias="destinationType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	protectionTimePeriod: Optional[TimePeriod] = Field(alias="protectionTimePeriod",default=None,)
	protectionUnitIds: Optional[list[str]] = Field(alias="protectionUnitIds",default=None,)
	restorePointPreference: Optional[RestorePointPreference | str] = Field(alias="restorePointPreference",default=None,)
	status: Optional[RestoreArtifactsBulkRequestStatus | str] = Field(alias="status",default=None,)
	tags: Optional[RestorePointTags | str] = Field(alias="tags",default=None,)

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
			if mapping_key == "#microsoft.graph.driveRestoreArtifactsBulkAdditionRequest":
				from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
				return DriveRestoreArtifactsBulkAdditionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxRestoreArtifactsBulkAdditionRequest":
				from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
				return MailboxRestoreArtifactsBulkAdditionRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.siteRestoreArtifactsBulkAdditionRequest":
				from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
				return SiteRestoreArtifactsBulkAdditionRequest.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .destination_type import DestinationType
from .public_error import PublicError
from .identity_set import IdentitySet
from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
from .restore_point_tags import RestorePointTags

