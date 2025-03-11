from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenApp(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bundleID: Optional[str] = Field(alias="bundleID",default=None,)


