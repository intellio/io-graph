from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AiInteractionContext(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	contextReference: Optional[str] = Field(alias="contextReference", default=None,)
	contextType: Optional[str] = Field(alias="contextType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)


