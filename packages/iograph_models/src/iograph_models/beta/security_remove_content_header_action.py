from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRemoveContentHeaderAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames",default=None,)


