from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class ConvertIdResult(BaseModel):
	errorDetails: Optional[Union[AccessReviewError]] = Field(alias="errorDetails", default=None,discriminator="odata_type", )
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	targetId: Optional[str] = Field(alias="targetId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_review_error import AccessReviewError
