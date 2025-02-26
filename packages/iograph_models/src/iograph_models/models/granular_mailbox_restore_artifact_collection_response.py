from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GranularMailboxRestoreArtifactCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[GranularMailboxRestoreArtifact] = Field(alias="value",)

from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact

