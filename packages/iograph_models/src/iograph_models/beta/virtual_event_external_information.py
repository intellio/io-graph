from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventExternalInformation(BaseModel):
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	externalEventId: Optional[str] = Field(alias="externalEventId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


