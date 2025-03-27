from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidMobileAppIdentifier(BaseModel):
	odata_type: Literal["#microsoft.graph.androidMobileAppIdentifier"] = Field(alias="@odata.type", default="#microsoft.graph.androidMobileAppIdentifier")
	packageId: Optional[str] = Field(alias="packageId", default=None,)


