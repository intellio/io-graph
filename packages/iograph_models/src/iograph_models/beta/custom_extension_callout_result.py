from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionCalloutResult(BaseModel):
	odata_type: Literal["#microsoft.graph.customExtensionCalloutResult"] = Field(alias="@odata.type", default="#microsoft.graph.customExtensionCalloutResult")
	calloutDateTime: Optional[datetime] = Field(alias="calloutDateTime", default=None,)
	customExtensionId: Optional[str] = Field(alias="customExtensionId", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	httpStatus: Optional[int] = Field(alias="httpStatus", default=None,)
	numberOfAttempts: Optional[int] = Field(alias="numberOfAttempts", default=None,)


