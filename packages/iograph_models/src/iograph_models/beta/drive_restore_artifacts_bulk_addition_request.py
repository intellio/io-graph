from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveRestoreArtifactsBulkAdditionRequest(BaseModel):
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
	directoryObjectIds: Optional[list[str]] = Field(alias="directoryObjectIds",default=None,)
	drives: Optional[list[str]] = Field(alias="drives",default=None,)

from .identity_set import IdentitySet
from .destination_type import DestinationType
from .public_error import PublicError
from .identity_set import IdentitySet
from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
from .restore_point_tags import RestorePointTags

