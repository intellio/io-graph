from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceAttributeQuestion(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	question: SerializeAsAny[Optional[AccessPackageQuestion]] = Field(alias="question",default=None,)

from .access_package_question import AccessPackageQuestion

