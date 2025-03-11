from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_virtual_appointment_join_web_urlGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


