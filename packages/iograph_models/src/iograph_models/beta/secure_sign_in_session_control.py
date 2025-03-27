from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecureSignInSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.secureSignInSessionControl"] = Field(alias="@odata.type", default="#microsoft.graph.secureSignInSessionControl")


