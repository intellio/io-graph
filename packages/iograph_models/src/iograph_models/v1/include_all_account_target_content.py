from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IncludeAllAccountTargetContent(BaseModel):
	type: Optional[AccountTargetContentType | str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .account_target_content_type import AccountTargetContentType

