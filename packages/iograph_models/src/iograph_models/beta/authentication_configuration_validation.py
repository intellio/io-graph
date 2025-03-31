from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AuthenticationConfigurationValidation(BaseModel):
	errors: Optional[list[Annotated[Union[AccessReviewError],Field(discriminator="odata_type")]]] = Field(alias="errors", default=None,)
	warnings: Optional[list[Annotated[Union[AccessReviewError],Field(discriminator="odata_type")]]] = Field(alias="warnings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_review_error import AccessReviewError
