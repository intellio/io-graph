from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PendingOperations(BaseModel):
	pendingContentUpdate: Optional[PendingContentUpdate] = Field(default=None,alias="pendingContentUpdate",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .pending_content_update import PendingContentUpdate

