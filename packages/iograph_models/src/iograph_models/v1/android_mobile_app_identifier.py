from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidMobileAppIdentifier(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	packageId: Optional[str] = Field(alias="packageId",default=None,)


