from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxRestoreArtifactCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[MailboxRestoreArtifact]]] = Field(alias="value",default=None,)

from .mailbox_restore_artifact import MailboxRestoreArtifact

