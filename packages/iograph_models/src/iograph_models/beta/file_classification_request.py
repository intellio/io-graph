from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileClassificationRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	file: Optional[str] = Field(alias="file",default=None,)
	sensitiveTypeIds: Optional[list[str]] = Field(alias="sensitiveTypeIds",default=None,)


