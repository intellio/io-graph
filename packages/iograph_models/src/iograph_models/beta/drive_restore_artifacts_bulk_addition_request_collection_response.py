from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveRestoreArtifactsBulkAdditionRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DriveRestoreArtifactsBulkAdditionRequest]] = Field(alias="value", default=None,)

from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
