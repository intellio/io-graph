from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_copy_from_content_type_hubPostRequest(BaseModel):
	contentTypeId: Optional[str] = Field(alias="contentTypeId",default=None,)


