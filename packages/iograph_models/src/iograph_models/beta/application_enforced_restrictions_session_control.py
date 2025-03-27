from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ApplicationEnforcedRestrictionsSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.applicationEnforcedRestrictionsSessionControl"] = Field(alias="@odata.type", default="#microsoft.graph.applicationEnforcedRestrictionsSessionControl")


