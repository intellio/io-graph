from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResultTemplateOption(BaseModel):
	enableResultTemplate: Optional[bool] = Field(default=None,alias="enableResultTemplate",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


