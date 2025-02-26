from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class RestoreArtifactBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	destinationType: Optional[DestinationType] = Field(default=None,alias="destinationType",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[ArtifactRestoreStatus] = Field(default=None,alias="status",)
	restorePoint: Optional[RestorePoint] = Field(default=None,alias="restorePoint",)

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
			if mapping_key == "#microsoft.graph.driveRestoreArtifact":
				from .drive_restore_artifact import DriveRestoreArtifact
				return DriveRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxRestoreArtifact":
				from .mailbox_restore_artifact import MailboxRestoreArtifact
				return MailboxRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.granularMailboxRestoreArtifact":
				from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
				return GranularMailboxRestoreArtifact.model_validate(data)
			if mapping_key == "#microsoft.graph.siteRestoreArtifact":
				from .site_restore_artifact import SiteRestoreArtifact
				return SiteRestoreArtifact.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .destination_type import DestinationType
from .public_error import PublicError
from .artifact_restore_status import ArtifactRestoreStatus
from .restore_point import RestorePoint

