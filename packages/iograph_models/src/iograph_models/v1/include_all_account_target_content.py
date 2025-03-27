from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IncludeAllAccountTargetContent(BaseModel):
	type: Optional[AccountTargetContentType | str] = Field(alias="type", default=None,)
	odata_type: Literal["#microsoft.graph.includeAllAccountTargetContent"] = Field(alias="@odata.type", default="#microsoft.graph.includeAllAccountTargetContent")

from .account_target_content_type import AccountTargetContentType

