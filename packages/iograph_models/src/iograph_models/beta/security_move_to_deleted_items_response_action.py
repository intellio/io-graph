from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMoveToDeletedItemsResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityEmailEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_email_entity_identifier import SecurityEmailEntityIdentifier

