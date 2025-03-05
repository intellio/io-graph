from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesProvisioningError(BaseModel):
	category: Optional[str] = Field(default=None,alias="category",)
	occurredDateTime: Optional[datetime] = Field(default=None,alias="occurredDateTime",)
	propertyCausingError: Optional[str] = Field(default=None,alias="propertyCausingError",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


