from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_global_script_highest_available_versionPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


