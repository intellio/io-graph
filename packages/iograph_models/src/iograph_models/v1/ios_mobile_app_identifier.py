from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IosMobileAppIdentifier(BaseModel):
	odata_type: Literal["#microsoft.graph.iosMobileAppIdentifier"] = Field(alias="@odata.type", default="#microsoft.graph.iosMobileAppIdentifier")
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)


