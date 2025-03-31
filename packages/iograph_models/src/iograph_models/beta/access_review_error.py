from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewError(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewError"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewError")

