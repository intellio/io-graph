from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SamlSingleSignOnSettings(BaseModel):
	relayState: Optional[str] = Field(alias="relayState", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


