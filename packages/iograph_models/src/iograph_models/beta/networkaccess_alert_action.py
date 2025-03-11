from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessAlertAction(BaseModel):
	actionLink: Optional[str] = Field(alias="actionLink",default=None,)
	actionText: Optional[str] = Field(alias="actionText",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


