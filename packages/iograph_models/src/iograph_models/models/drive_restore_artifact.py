from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveRestoreArtifact(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	destinationType: Optional[DestinationType] = Field(default=None,alias="destinationType",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[ArtifactRestoreStatus] = Field(default=None,alias="status",)
	restorePoint: Optional[RestorePoint] = Field(default=None,alias="restorePoint",)
	restoredSiteId: Optional[str] = Field(default=None,alias="restoredSiteId",)
	restoredSiteName: Optional[str] = Field(default=None,alias="restoredSiteName",)
	restoredSiteWebUrl: Optional[str] = Field(default=None,alias="restoredSiteWebUrl",)

from .destination_type import DestinationType
from .public_error import PublicError
from .artifact_restore_status import ArtifactRestoreStatus
from .restore_point import RestorePoint

