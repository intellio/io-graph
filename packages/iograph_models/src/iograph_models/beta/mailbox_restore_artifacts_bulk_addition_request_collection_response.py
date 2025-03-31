from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailboxRestoreArtifactsBulkAdditionRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MailboxRestoreArtifactsBulkAdditionRequest]] = Field(alias="value", default=None,)

from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
