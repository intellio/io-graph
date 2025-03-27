from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PendingOperations(BaseModel):
	pendingContentUpdate: Optional[PendingContentUpdate] = Field(alias="pendingContentUpdate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .pending_content_update import PendingContentUpdate

