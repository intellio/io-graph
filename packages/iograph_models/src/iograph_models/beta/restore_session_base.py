from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RestoreSessionBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	restoreJobType: Optional[RestoreJobType | str] = Field(alias="restoreJobType",default=None,)
	restoreSessionArtifactCount: Optional[RestoreSessionArtifactCount] = Field(alias="restoreSessionArtifactCount",default=None,)
	status: Optional[RestoreSessionStatus | str] = Field(alias="status",default=None,)

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
			if mapping_key == "#microsoft.graph.exchangeRestoreSession":
				from .exchange_restore_session import ExchangeRestoreSession
				return ExchangeRestoreSession.model_validate(data)
			if mapping_key == "#microsoft.graph.oneDriveForBusinessRestoreSession":
				from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
				return OneDriveForBusinessRestoreSession.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointRestoreSession":
				from .share_point_restore_session import SharePointRestoreSession
				return SharePointRestoreSession.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .restore_job_type import RestoreJobType
from .restore_session_artifact_count import RestoreSessionArtifactCount
from .restore_session_status import RestoreSessionStatus

