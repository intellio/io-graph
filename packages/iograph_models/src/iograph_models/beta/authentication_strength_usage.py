from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationStrengthUsage(BaseModel):
	mfa: Optional[list[Annotated[Union[ConditionalAccessWhatIfPolicy]],Field(discriminator="odata_type")]]] = Field(alias="mfa", default=None,)
	none: Optional[list[Annotated[Union[ConditionalAccessWhatIfPolicy]],Field(discriminator="odata_type")]]] = Field(alias="none", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy

