from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationJobSubject(BaseModel):
	links: Optional[SynchronizationLinkedObjects] = Field(alias="links",default=None,)
	objectId: Optional[str] = Field(alias="objectId",default=None,)
	objectTypeName: Optional[str] = Field(alias="objectTypeName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_linked_objects import SynchronizationLinkedObjects

