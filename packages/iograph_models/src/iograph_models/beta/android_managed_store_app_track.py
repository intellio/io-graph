from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreAppTrack(BaseModel):
	trackAlias: Optional[str] = Field(alias="trackAlias",default=None,)
	trackId: Optional[str] = Field(alias="trackId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


