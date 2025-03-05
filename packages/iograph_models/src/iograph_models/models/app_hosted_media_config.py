from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppHostedMediaConfig(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	blob: Optional[str] = Field(default=None,alias="blob",)


