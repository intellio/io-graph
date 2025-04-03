from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DriveRestoreArtifact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.driveRestoreArtifact"] = Field(alias="@odata.type", default="#microsoft.graph.driveRestoreArtifact")
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	destinationType: Optional[DestinationType | str] = Field(alias="destinationType", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[ArtifactRestoreStatus | str] = Field(alias="status", default=None,)
	restorePoint: Optional[RestorePoint] = Field(alias="restorePoint", default=None,)
	restoredSiteId: Optional[str] = Field(alias="restoredSiteId", default=None,)
	restoredSiteName: Optional[str] = Field(alias="restoredSiteName", default=None,)
	restoredSiteWebUrl: Optional[str] = Field(alias="restoredSiteWebUrl", default=None,)

from .destination_type import DestinationType
from .public_error import PublicError
from .artifact_restore_status import ArtifactRestoreStatus
from .restore_point import RestorePoint
