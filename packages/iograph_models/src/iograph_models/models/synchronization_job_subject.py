from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJobSubject(BaseModel):
	links: Optional[SynchronizationLinkedObjects] = Field(default=None,alias="links",)
	objectId: Optional[str] = Field(default=None,alias="objectId",)
	objectTypeName: Optional[str] = Field(default=None,alias="objectTypeName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_linked_objects import SynchronizationLinkedObjects

