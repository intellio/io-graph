from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersonNamePronounciation(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	first: Optional[str] = Field(alias="first",default=None,)
	last: Optional[str] = Field(alias="last",default=None,)
	maiden: Optional[str] = Field(alias="maiden",default=None,)
	middle: Optional[str] = Field(alias="middle",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


