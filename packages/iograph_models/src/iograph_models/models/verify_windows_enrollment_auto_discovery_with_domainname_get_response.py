from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Verify_windows_enrollment_auto_discovery_with_domainnameGetResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


