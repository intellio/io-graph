from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventExternalInformation(BaseModel):
	applicationId: Optional[str] = Field(default=None,alias="applicationId",)
	externalEventId: Optional[str] = Field(default=None,alias="externalEventId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


