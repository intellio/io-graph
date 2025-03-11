from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OneDriveForBusinessRestoreSession(BaseModel):
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
	driveRestoreArtifacts: Optional[list[DriveRestoreArtifact]] = Field(alias="driveRestoreArtifacts",default=None,)
	driveRestoreArtifactsBulkAdditionRequests: Optional[list[DriveRestoreArtifactsBulkAdditionRequest]] = Field(alias="driveRestoreArtifactsBulkAdditionRequests",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .restore_job_type import RestoreJobType
from .restore_session_artifact_count import RestoreSessionArtifactCount
from .restore_session_status import RestoreSessionStatus
from .drive_restore_artifact import DriveRestoreArtifact
from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest

