from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRemoveContentFooterAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.removeContentFooterAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.removeContentFooterAction")
	uiElementNames: Optional[list[str]] = Field(alias="uiElementNames", default=None,)


