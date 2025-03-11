from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_file_vault_keyGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


