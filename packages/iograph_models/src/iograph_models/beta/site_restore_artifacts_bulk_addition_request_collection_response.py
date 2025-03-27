from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SiteRestoreArtifactsBulkAdditionRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SiteRestoreArtifactsBulkAdditionRequest]] = Field(alias="value", default=None,)

from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

