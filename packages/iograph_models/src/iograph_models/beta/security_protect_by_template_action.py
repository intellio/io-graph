from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProtectByTemplateAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)


