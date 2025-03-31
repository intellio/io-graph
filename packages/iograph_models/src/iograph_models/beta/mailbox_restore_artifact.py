from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class MailboxRestoreArtifact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	destinationType: Optional[DestinationType | str] = Field(alias="destinationType", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[ArtifactRestoreStatus | str] = Field(alias="status", default=None,)
	restorePoint: Optional[RestorePoint] = Field(alias="restorePoint", default=None,)
	restoredFolderId: Optional[str] = Field(alias="restoredFolderId", default=None,)
	restoredFolderName: Optional[str] = Field(alias="restoredFolderName", default=None,)
	restoredItemCount: Optional[int] = Field(alias="restoredItemCount", default=None,)

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
			if mapping_key == "#microsoft.graph.granularMailboxRestoreArtifact":
				from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
				return GranularMailboxRestoreArtifact.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .destination_type import DestinationType
from .public_error import PublicError
from .artifact_restore_status import ArtifactRestoreStatus
from .restore_point import RestorePoint
