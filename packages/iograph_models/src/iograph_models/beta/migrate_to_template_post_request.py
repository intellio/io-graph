from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Migrate_to_templatePostRequest(BaseModel):
	newTemplateId: Optional[str] = Field(alias="newTemplateId",default=None,)
	preserveCustomValues: Optional[bool] = Field(alias="preserveCustomValues",default=None,)


