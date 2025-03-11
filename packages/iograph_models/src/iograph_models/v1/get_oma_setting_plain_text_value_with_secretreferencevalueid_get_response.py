from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_oma_setting_plain_text_value_with_secretreferencevalueidGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


